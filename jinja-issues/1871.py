import jinja2
env = jinja2.Environment(undefined=jinja2.DebugUndefined)

print(env.from_string(
    "env.val is {{ env.val }} 1"
).render({'env': {'val': 'something'}}))

print(env.from_string(
    "env.val is {{ env.val }} 2"
).render({'env': {}}))

# This is the error
print(env.from_string(
    "env.val is {{ env.val }} 3"
).render({'other': 'something'}))
