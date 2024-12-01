import jinja2


ENVIRONMENT = jinja2.Environment(loader=jinja2.BaseLoader())

WORKING_TEMPLATE = ENVIRONMENT.from_string("{{ self_ }}")
BROKEN_TEMPLATE = ENVIRONMENT.from_string("{{ self }}")

print("Works:", WORKING_TEMPLATE.render({"self_": ":)"}))
print("Doesn't work:", BROKEN_TEMPLATE.render({"self": ":("}))
