from jinja2 import Environment

import json

env = Environment()
env.filters["rawjson"] = json.dumps

t = env.from_string("{{ x|rawjson }} <p></p>")

print(t.render(x={"html": "<p class=\"this\"> foo and 'bar' </p>"}))
# print(t.render(x="<bar>"))

# value = "'"
# print(json.dumps(value))
