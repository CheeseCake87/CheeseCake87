from jinja2 import Environment
from markupsafe import Markup
import json

env = Environment()

t = env.from_string("{{ x|tojson }}")

print(t.render(x={"html": "<p class=\"this\"> foo and 'bar' </p>"}))
# print(t.render(x="<bar>"))

value = "<p class=\"this\"> foo and 'bar' </p>"
print(json.dumps(value))
