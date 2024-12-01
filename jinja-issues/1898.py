import textwrap

from jinja2 import DictLoader, Environment, select_autoescape

TEMPLATES = {
    'base.html': textwrap.dedent('''
        Subject: 
        {% block subject %}{% endblock %}
        Body: {% block body %}{% endblock %}
    ''').strip(),
    'test1.html': textwrap.dedent('''
        {% extends 'base.html' %}
        {% block subject %}{{ text }}{% endblock %}
        {% block body %}{{ text }}{% endblock %}
    ''').strip(),
    'test2.html': textwrap.dedent('''
        {% extends 'base.html' %}
        {% autoescape false -%}
            {% block subject %}{{ text }}{% endblock %}
        {%- endautoescape %}
        {% block body %}{{ text }}{% endblock %}
    ''').strip(),
    'test3.html': textwrap.dedent('''
        {% extends 'base.html' %}
        {% block subject %}
            {%- autoescape false %}{{ text }}{% endautoescape -%}
        {% endblock %}
        {% block body %}{{ text }}{% endblock %}
    ''').strip(),
}

TEXT = "hel'lo"

env = Environment(loader=DictLoader(TEMPLATES), autoescape=select_autoescape())
print('test1')
print(env.get_template('test1.html').render(text=TEXT))
print()
print('test2')
print(env.get_template('test2.html').render(text=TEXT))
print()
print('test3')
print(env.get_template('test3.html').render(text=TEXT))
