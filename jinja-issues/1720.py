from jinja2 import Environment

env = Environment()
env.globals = {"x": 2}
out = env.from_string("{{ -1 ** x }}").render()
print(out)
