import jinja2
import jinja2.sandbox
import os

TEMPLATE_FILE = './test.j2'
OUT_FILE = './test.txt'

def main():
    loader = jinja2.FileSystemLoader(os.path.dirname('.'))
    jinja_env = jinja2.sandbox.SandboxedEnvironment()

    # Open the template
    with open(TEMPLATE_FILE, 'r') as template_file:
        template = jinja_env.from_string(template_file.read())

    # Assign the finished string to 'output'
    output = template.render()

    with open(OUT_FILE, 'w') as outfile:
        outfile.write(output)

if __name__ == '__main__':
    main()