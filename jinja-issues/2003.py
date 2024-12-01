from jinja2 import Template

inner = (
    Template(
        '<b>{{ first_name }}</b> {{ last_name }}',
        autoescape=True
    )
    .render(first_name='John', last_name="Doe"))

outer = (
    Template(
        'Hello,<br/>{{ name }}!',
        autoescape=True
    )
    .render(name=inner))

print(inner)
print("-"*10)
print(outer)
