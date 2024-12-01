import jinja2
environment = jinja2.Environment()
jinja_template = """
    {%- for name in names %}
        ("HELLO {{name}}!")
    {%- endfor %}
"""
template = environment.from_string(jinja_template)
data = template.render(names=None)
print(data)