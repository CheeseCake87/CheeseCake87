from jinja2.nativetypes import NativeEnvironment

env = NativeEnvironment()
out = env.from_string("""
        {% block test %}
            {% for i in range(1) %}
                {{ loop.index }}
            {% endfor %}
        {% endblock %}
        """).render()

print(out)
