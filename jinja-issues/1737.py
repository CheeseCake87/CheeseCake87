from jinja2 import Environment
from pathlib import Path

htmlTemplatePath = Path(__file__).parent / "templates" / "template.html"

env = Environment()

with open(htmlTemplatePath, 'r') as f:
   htmlTemplate = env.from_string(f.read())

output = htmlTemplate.render()

print(output)
