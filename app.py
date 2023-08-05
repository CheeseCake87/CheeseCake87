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
