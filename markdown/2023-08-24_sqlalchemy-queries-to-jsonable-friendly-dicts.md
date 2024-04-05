```
Publish: True
Date: 2023-08-24 10:24:53 +0100
Title: "SQLAlchemy queries to JSONable friendly dicts"
Description: "Exploring methods of converting SQLAlchemy queries to JSONable dicts because I'm lazy."
```

As of Flask 1.1, I believe; you have been able to simply return a
dict from a route, which will be converted to a JSON response.

Here's an example:

```python
@app.route('/api')
def api():
    return {'hello': 'world'}
```

Simple, right? But what if you want to return a query from a database?

```python
@app.route('/api')
def api():
    from app.models.whatever import Whatever
    from app import db
    result = db.session.execute(
        db.select(Whatever).filter_by(Whatever.thing_id == 1)
    ).scalars().all()
    data = {}
    for item in result:
        data[item.id] = {
            'name': item.name,
            'description': item.description,
            'created_at': item.created_at,
            'updated_at': item.updated_at
        }
    return data
```

This is probably the first thing you would try, and it works.

Personally, I prefer to keep all query-like logic in the models.

```python
# app/models/whatever.py

from app import db


class Whatever(db.Model):
    thing_id = db.Column(...)
    name = db.Column(...)
    description = db.Column(...)
    created_at = db.Column(...)
    updated_at = db.Column(...)

    @classmethod
    def get_by_id(cls, thing_id):
        return db.select(
            Whatever
        ).filter_by(
            Whatever.thing_id == 1
        ).scalars().all()

```

Would then allow for:

```python
@app.route('/api')
def api():
    from app.models.whatever import Whatever
    data = {}
    for item in Whatever.get_by_id(1):
        data[item.id] = {
            'name': item.name,
            'description': item.description,
            'created_at': item.created_at,
            'updated_at': item.updated_at
        }
    return data
```

A little cleaner, but you are still having to define
values in the return data. `item.name`, `item.description`, Etc...

You are able to use the in-built `_asdict()` method of the SQLAlchemy on each row.

```python
@app.route('/api')
def api():
    from app.models.whatever import Whatever
    data = {}
    for item in Whatever.get_by_id(1):
        data[item.id] = item._asdict()
    return data
```

However, this method does not work with rows that are the result of a join.

It is said, whether true or not, that the lazy programmer is the best programmer.
I'm not sure if this should be a method of thought to live by; But it does promote
DRY code, and I don't want to keep defining columns in the return data if I don't have to.

So my solution was a mixin class that has two methods. `as_jsonable_dict` and `as_json`

```python
import json
import typing as t
from datetime import datetime

from sqlalchemy import Result
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.engine import Row


class JSONMixin:

    @classmethod
    def as_jsonable_dict(
            cls,
            execute: Result,
            include_joins: list = None,
            all_columns_but: list = None,
            only_columns: list = None,
    ) -> t.Dict[str, t.List[t.Dict[str, t.Any] | None]]:
        """
        Expects: execute = db.session.execute(query)

        execute is run with .scalars() and .all() to get the results

        execute.scalars().all()
        """

        if include_joins is None:
            include_joins = []

        if all_columns_but is None:
            all_columns_but = []

        if only_columns is None:
            only_columns = []

        def include_column(column):
            if only_columns:
                if column not in only_columns:
                    return False

            if all_columns_but:
                if column in all_columns_but:
                    return False

            return True

        def as_dict(row: Row) -> dict:
            return {key: row.__dict__[key] for key in row.__dict__ if key[0] != '_'}

        def parse_value(value):
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d %H:%M:%S")

            if isinstance(value, int) or isinstance(value, bool) or isinstance(value, str):
                return value

            if isinstance(value, t.Iterable):
                if isinstance(value, dict):
                    return {key: parse_value(x) for key, x in value.items()}

                return [parse_value(x) for x in value]

            return f"{value}"

        def parse_row(row: Row, _is_join: bool = False):
            data = dict()
            for column, value in as_dict(row).items():
                if not include_column(column):
                    continue

                if isinstance(value, InstrumentedList):
                    continue

                data[column] = parse_value(value)

            if _is_join:
                return data

            joins = dict()
            for join in include_joins:
                if hasattr(row, join):
                    joins[join] = [parse_row(row, _is_join=True) for row in getattr(row, join)] or []

            return data, joins

        def parse(query_row: Row):
            data, joins = parse_row(query_row)
            return {**data, **joins}

        return {cls.__name__: [parse(x) for x in execute.scalars().all()]}

    @classmethod
    def as_json(
            cls,
            execute: Result,
            include_joins: list = None,
            all_columns_but: list = None,
            only_columns: list = None,
    ) -> str | None:
        return json.dumps(cls.as_jsonable_dict(
            execute,
            include_joins=include_joins,
            all_columns_but=all_columns_but,
            only_columns=only_columns,
        ))
```

This solution uses `Row.__dict__` to get the columns and values of the row, and this
also includes the columns that are the result of a join.

The `as_jsonable_dict` method is the one that does the heavy lifting. It expects
a SQLAlchemy `Result` object, which is the result of `db.session.execute(query)`.

Here is an example of its usage in a classmethod:

```python
@classmethod
def get_by_id(cls, thing_id) -> dict:
    query = select(cls).filter_by(user_id=thing_id)
    return cls.as_jsonable_dict(
        db.session.execute(query)
    )
```

This will then return:

```
{
    "Whatever": [
        {colmun: value, ...}, {colmun: value, ...}
    ]
}
```

The `as_json` method is just a wrapper for `json.dumps` and `as_jsonable_dict`. It returns the same as
the above but uses the in-built json module to convert the dict to a JSON string.

A standalone example of this can be found in the following Gist
[https://gist.github.com/CheeseCake87/20398198f2b388e27b396cdbb92cfe56](https://gist.github.com/CheeseCake87/20398198f2b388e27b396cdbb92cfe56)

In the Gist it also gives an example of using this mixin with joins. The `include_joins` argument
takes a list of any relationship attributes that have been created.

I have included some arguments to deal with limiting the columns returned. `all_columns_but` and `only_columns`

`all_columns_but` will exclude any columns that are in the list. `only_columns`
will only include columns that are in the list. This effects the joins too!

The Gist uses the example models Users, Cars and Boats, and demonstrates how joins can be included.

```python
# relationships
rel_cars = db.relationship(
    "Cars",
    primaryjoin="Users.user_id == Cars.fk_user_id"
)
rel_boats = db.relationship(
    "Boats",
    primaryjoin="Users.user_id == Boats.fk_user_id"
)


@classmethod
def get_by_id(cls, user_id):
    query = select(cls).filter_by(user_id=user_id)

    return cls.as_jsonable_dict(
        db.session.execute(query),
        include_joins=["rel_cars", "rel_boats"],
    )
```

Results in:

```
{
    "Users": [
        {
            "created": "2023-08-24 09:53:05",
            "user_id": 1,
            "updated": "None",
            "username": "user1",
            "rel_cars": [
                {
                    "updated": "None",
                    "make": "Ford",
                    "created": "2023-08-24 09:53:05",
                    "car_id": 1,
                    "fk_user_id": 1
                },
                {
                    "updated": "None",
                    "make": "Mazda",
                    "created": "2023-08-24 09:53:05",
                    "car_id": 2,
                    "fk_user_id": 1
                }
            ],
            "rel_boats": [
                {
                    "fk_user_id": 1,
                    "created": "2023-08-24 09:53:05",
                    "make": "Big",
                    "boat_id": 1,
                    "stats": {
                        "length": 100
                    },
                    "updated": "None"
                }
            ]
        }
    ]
}
```

Now our route can be as simple as:

```python
@app.route('/api')
def api():
    from app.models.whatever import Whatever
    return {
        "status": "success",
        **Whatever.get_by_id(1)
    }
```

Which will return:

```
{
    "status": "success",
    "Whatever": [
        {
            "thing_id": 1,
            "name": "Thing 1",
            "description": "This is thing 1",
            "created_at": "2023-08-24 09:53:05",
            "updated_at": "None"
        }
    ]
}
```

I've not used this in production yet, I suspect there will be some stumbling in doing so.
But the result so far is a much easier way to get JSON friendly data from a query.

https://github.com/jonbiemond helped me prune the code a little, cutting away some of the
unnecessary code, and making it a little more readable.

We also discussed the architecture of how to get dicts from a query. One of my earlier methods
chosen was to use the `_asdict` private method of the `Row` object. This returns a dict of the
row. However, this method is missing from rows that are the result of a join as I mentioned, 
so I had to take a different approach.

The method used in the mixin is a little more verbose, in regard to including joins,
but it does allow for the inclusion of joins in a more explicit way, I suppose.

You may have already been aware of another more popular library
that does this exact thing called [Marshmallow](https://marshmallow.readthedocs.io/en/stable/).

I guess the main difference between this mixin solution and Marshmallow is that Marshmallow is agnostic, and requires
some boilerplate code to get going.

Hopefully this is useful to someone, and if you have any suggestions or improvements, please comment on the gist.

Thanks for reading.
BYEEEEEEEEEEEEEEEEEEEeeee.

_SQLAlchemy queries to JSONable friendly dicts by David Carmichael_