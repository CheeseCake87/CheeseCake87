from jinja2 import Environment, select_autoescape

env = Environment(autoescape=select_autoescape())

output = env.from_string("{{ '<' }}").render()

print(output)
