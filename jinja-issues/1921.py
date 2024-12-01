from jinja2 import Environment

env = Environment()

template = """\
{{ '31e1170' | int(base=16) }}
"""

output = env.from_string(template).render()

print(output)
