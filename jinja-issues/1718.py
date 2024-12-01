from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("1718"))
env.add_extension("jinja2.ext.debug")

output = env.get_template("template.html").render()

print(output)
