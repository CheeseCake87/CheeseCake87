from textwrap import dedent

from jinja2 import Environment, pass_context


def main():
    env = Environment()

    @pass_context
    def is_foo(ctx, s):
        return s == "bar"

    # env.tests["foo"] = is_foo

    output = env.from_string(dedent(
"""
{% set x = ["one", "foo" ] %}
{{ x | select("foo") }}

{{ [1, 2, 3] }}
{{ [1, 2, 3]|select("divisibleby", 3) }}
"""
        )).render({})

    print(output)


if __name__ == "__main__":
    main()
