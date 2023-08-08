title="Flask as a Static Site Generator";
description="Using Flask as a static site generator.";
date="2023-08-06 15:00:00 +0100";

::::

**Update: This project has changed a lot since this post was written. Please visit the GitHub page to see the changes.**

[https://github.com/CheeseCake87/CheeseCake87](https://github.com/CheeseCake87/CheeseCake87)

Hey guys! / folks! / [insert whatever cool kid greeting here]!

So I made a static site generator using Flask. Which is used to generate this site.

It's a single `app.py` file that is 85 lines long. Including that blank line that the IDE keeps complaining about when
coding in Python.

Here's the needed folder structure:

```text
├── docs/
│   ├── static/
│   │   └── ...
│   └── ...
├── markdown/
│   └── 2023-08-06:flask-as-a-static-site-generator.md
├── templates/
│   ├── __main__.html
│   └── index.html
└── app.py
```

Here's the `app.py`:

```python
from pathlib import Path

import mistune
from flask import Flask, render_template
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            if info == "jinja2":
                info = "jinja"
            try:
                lexer = get_lexer_by_name(info, stripall=True)
            except ClassNotFound:
                lexer = get_lexer_by_name('text', stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return '<pre><code>' + mistune.escape(code) + '</code></pre>'


cwd = Path(__file__).parent


def get_docs_files(docs_dir: Path) -> list:
    _ = []
    for f in docs_dir.glob("*.html"):
        if f.stem == "index":
            continue
        _.append(f.stem)

    return _


def compiler(re_compile=False):
    docs_dir = cwd / "docs"
    markdown_dir = cwd / "markdown"

    index = docs_dir / "index.html"

    docs_dir_files = get_docs_files(docs_dir)
    markdown_dir_files = markdown_dir.glob("*.md")

    if re_compile:
        for file in docs_dir_files:
            (docs_dir / f"{file}.html").unlink()

    for file in markdown_dir_files:
        if file.stem not in docs_dir_files or re_compile:
            markdown = mistune.Markdown(renderer=HighlightRenderer())
            with open(docs_dir / f"{file.stem}.html", mode="w") as f:
                split = file.stem.split(":")
                f.write(render_template(
                    "__main__.html",
                    title=split[1],
                    date=split[0],
                    content=markdown(file.read_text())
                ))

    index.write_text(
        render_template(
            "index.html",
            pages=get_docs_files(docs_dir)
        )
    )


def create_app():
    app = Flask(__name__)
    app.static_folder = "static"
    app.template_folder = "templates"

    @app.cli.command("compile")
    def compile_site():
        compiler()

    @app.cli.command("re-compile")
    def re_compile_site():
        compiler(re_compile=True)

    return app
```

If you can't work it out from the code, here's how it works:

Running `flask compile`

1. It gets all the markdown files in the `markdown/` folder.
2. It pulls the title and the date from the filename of the markdown file. "-" in the title is replaced with a
   space, "-" are better for URLs, so the internet says...
3. It then gets all the html files in the `docs/` folder.
4. It then compares the two lists, and if there is a markdown file that doesn't have a corresponding html file, it
   generates the html file.
5. It then generates the `index.html` file with all the links to the other pages.

Running `flask re-compile` will do the same thing, but it will delete all the html files in the `docs/` folder first.

This project sits on my main GitHub repo, ya know the one that is the same as your username, here's the link:
[https://github.com/CheeseCake87/CheeseCake87](https://github.com/CheeseCake87/CheeseCake87)

The project contains the template files and the static files, so you can see how it works.

The html is being saved in the docs folder, because GitHub pages uses that folder to serve the site. The site is then
setup with the domain name thecodingside.quest, which was surprisingly cheap to register.

OK, Bye.

_Flask As A Static Site Generator by David Carmichael_
