from jinja2 import Environment, FileSystemLoader, ext
from jinja2.ext import Extension
from jinja2.lexer import Token, TOKEN_VARIABLE_BEGIN, TOKEN_VARIABLE_END


class LatexEscapeExtension(Extension):
    def filter_stream(self, stream):
        for token in stream:
            if token.type == TOKEN_VARIABLE_BEGIN:
                yield token
                yield Token(token.lineno, 'lparen', '(')
            elif token.type == TOKEN_VARIABLE_END:
                yield Token(token.lineno, 'rparen', ')')
                yield Token(token.lineno, 'pipe', '|')
                yield Token(token.lineno, 'name', 'escape_tex')
                yield token
            else:
                yield token


# Define the LaTeX escaping filter
def escape_tex(value):
    escape_map = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    return ''.join(escape_map.get(char, char) for char in value)


# Set up the Jinja environment and register the custom extension and filter
env = Environment(loader=FileSystemLoader('templates'), extensions=[LatexEscapeExtension])
env.filters['escape_tex'] = escape_tex

# Sample template string with LaTeX special characters
template_str = """
This is a LaTeX document with a variable: {{ variable }}
"""

# Create the template
template = env.from_string(template_str)

# Render the template with a sample value containing LaTeX special characters
output = template.render(variable="100% safe & secure $5 deal with #1 quality")

print(output)