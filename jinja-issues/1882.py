import json

from jinja2 import Environment

env = Environment()

foo = {'foo': 'test="</script>" attack'}
foo_json = json.dumps(foo)

cars = [
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    {
        "make": "Chevy",
        "model": "Camaro",
        "year": 1969
    },
    {
        "unsafe": "foo</script><script>alert('pwnd!');</script><script>bar;"
    }
]

_js_escapes = {
    ord('\\'): '\\u005C',
    ord('\''): '\\u0027',
    ord('"'): '\\u0022',
    ord('>'): '\\u003E',
    ord('<'): '\\u003C',
    ord('&'): '\\u0026',
    ord('='): '\\u003D',
    ord('-'): '\\u002D',
    ord(';'): '\\u003B',
    ord('\u2028'): '\\u2028',
    ord('\u2029'): '\\u2029'
}

template = """
{{ foo | tojson }}
"""

output = env.from_string(template).render(
    foo=foo_json,
)

print(output)
