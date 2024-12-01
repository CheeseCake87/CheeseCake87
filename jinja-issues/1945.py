from jinja2 import Environment

env = Environment()

template = '''\
{{ "lorem ipsum 'example.org'." | urlize }}
'''

output = env.from_string(template).render()

print(output)