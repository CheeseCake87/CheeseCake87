### Namespace multi-variable assignment:

[https://github.com/pallets/jinja/issues/1413](https://github.com/pallets/jinja/issues/1413)

|LATER|

Makes sense to include, a task for later.

---

### Loop-variables are not accessible in @pass_context / @contextfilter

https://github.com/pallets/jinja/issues/1478

|LATER|

Suggested lost of speed if included. Maybe make this a feature flag?

Would require investigation and more code than you likely think.

---

### Can't use a test decorated with `@pass_context` in `select`

https://github.com/pallets/jinja/issues/1624

|UNSURE|

Unable to get example working.

---

### Add searchpath to TemplateNotFound exception message

https://github.com/pallets/jinja/issues/1661

|INCLUDE|

This one looks like a good one to include, or to think about.

---

### Faulty handling of UNC paths (pathlib in PackageLoader)

https://github.com/pallets/jinja/issues/1675

|LATER|

Suggested code changes in a tag:
https://github.com/UlrichEckhardt/jinja/releases/tag/jfrog-dev1

Haven't looked at this. It's one for later.

---

### `lexer.Token.value` has wrong type

https://github.com/pallets/jinja/issues/1687

|CLOSE|

Typing issue, looks like it has already changed to `t.Any`

It really should be `t.Union[str, int, float]` (for prior python support)

---

### `Failure.__call__` provides wrong arguments to `self.error_class`

https://github.com/pallets/jinja/issues/1688

|CLOSE|

Look like this is correct:
`lexer.py > line 266`
`exceptions.py > line 91`

There's no kwargs used so the order looks out, but it looks like
`exceptions.py > line 115` does some checking for this. So maybe a close? -
wouldn't be a big task to be explicit here though.

---

### TypeError: sequence item 0: expected str instance, int found

https://github.com/pallets/jinja/issues/1701

|CLOSE|

Looks like this only happens when using `NativeEnvironment`, I tested using
`Environment` and the code worked fine.

Ah, OK. `NativeEnvironment().from_string` looks like the issue.

This works:

```
from jinja2.nativetypes import NativeEnvironment

env = NativeEnvironment()
out = env.from_string("""
        {% block test %}
            {% for i in range(1) %}
                {{ loop.index }}
            {% endfor %}
        {% endblock %}
        """).render()

print(out)
```

---

### The error message from PackageLoader could be more helpful

https://github.com/pallets/jinja/issues/1705

|INCLUDE|

`ValueError: The '1705' package was not installed in a way that PackageLoader understands.`
is set in `loaders.py > line 326` Which could do with a better explination or
the error, if possible.

---

### debug extension pprinting in html

https://github.com/pallets/jinja/issues/1718

|INVESTIGATE|

Possible Close.
Not really sure if I understand what the request is here. Do they want to
remove the pprint line break seen after values? - Not sure about this, looks
like it might just be a close.

---

### Negative number raised to even power gives negative result if exponent is a variable

https://github.com/pallets/jinja/issues/1720

|INCLUDE|

If time is available. `**` math issue

---

### Bug with right-left associativity of exponent

https://github.com/pallets/jinja/issues/1722

|INCLUDE|

Looks like this is related to the issue above. May be worth just doing it...

---

### Missing line info from syntax error message

https://github.com/pallets/jinja/issues/1737

|CLOSE|

This is asking for better error messaging. I would close with a message that
this might be included in a future version, but no plans for it at the moment.

---

### Template caching does not take environment configuration into account

[https://github.com/pallets/jinja/issues/1738](https://github.com/pallets/jinja/issues/1738)

|LATER|

Large job that requires redesign.

---

### explain associativity and precedence between operators

https://github.com/pallets/jinja/issues/1755

|INCLUDE|

Related to [#379](https://github.com/pallets/jinja/issues/379) - Write docs to
explain operators

---

### Configurable behavior when translated string interpolation fails.

https://github.com/pallets/jinja/issues/1763

|UNSURE|

Not entirely sure on what this is talking about, I'm not familiar with
translation strings.

---

### Contains as a new Test (flipped operation of in)
https://github.com/pallets/jinja/issues/1766

|LATER|

This is a feature request, set aside for later. They would like to see:
`['Mike','Joe','Michael'] | select('contains', 'Mi') | list` returning 
`['Mike', 'Michael']`

---

### Undefined name `autoescape` in custom filter example
https://github.com/pallets/jinja/issues/1769

|INCLUDE|

Accurate, Docs update required.

[https://jinja.palletsprojects.
com/en/stable/api/#custom-filters:~:text=the%20output%20safe.-,import%20re,-from%20jinja2%20import](https://jinja.palletsprojects.com/en/stable/api/#custom-filters:~:text=the%20output%20safe.-,import%20re,-from%20jinja2%20import)

---

### Support accurate dependency tracking including dynamic inheritance or inclusion
https://github.com/pallets/jinja/issues/1775

|INVESTIGATE|

Wants to dynamically inheriting `jinja2.meta.find_referenced_templates`

I'm not sure on the use case of this...

---

### unique filter does not work when chain with a filter that returns async generator
https://github.com/pallets/jinja/issues/1781

|LATER|

I suspect this won't be easy to implement. Maybe for the eventual re-write?
Needs a complete code example.

---

### f-string sytax error when importing macro in a template which filename is also a template
https://github.com/pallets/jinja/issues/1792

|INCLUDE|

If possible. This is related to the security issue with filenames:

https://github.com/pallets/jinja/security/advisories/GHSA-gmj6-6f8f-6699

---

### Extension: Support saving arbitrary data with AssignmentBlock
https://github.com/pallets/jinja/issues/1803

|LATER|

This is related to a closed issue: https://github.com/pallets/jinja/issues/714

The person that has made this issue has offered to do a PR, maybe leave a 
comment asking if they will still be interested?

---

### Docs update re triple quotes and block assignments
https://github.com/pallets/jinja/issues/1825

|INCLUDE|

Documentation update that makes sense.

---

### Enhance Default Exceptions to include Line Number.
https://github.com/pallets/jinja/issues/1861

|CLOSE|

This looks like it has been done?

I ran the code and got `File "<template>", line 2, in top-level template code`

That looks like a line number to me.

---

### Allow passing multiple templates to import, just like include
https://github.com/pallets/jinja/issues/1862

|LATER|

This a potential close. It's a feature request that would be more suited to 
a re-write.

---

### DebugUndefined does not handle object.value replacements
https://github.com/pallets/jinja/issues/1871

|INCLUDE|

This makes sense to include in an upcoming release. Although maybe my 
understanding of what the `DebugUndefined` class does is incorrect.

The request here is that when the `DebugUndefined` class is used, it should
not raise an error when `object.value` is used, but instead should return
`<Undefined>`.

---

### Escape newlines for tojson filter as Django
https://github.com/pallets/jinja/issues/1882

---