from pathlib import Path

from flask import Flask, render_template

import markdown

cwd = Path(__file__).parent


def compiler(re_compile=False):
    docs_dir = cwd / "docs"
    markdown_dir = cwd / "markdown"

    docs_dir_files = [f.stem for f in docs_dir.glob("*.html")]
    markdown_dir_files = markdown_dir.glob("*.md")

    for file in markdown_dir_files:
        if file.stem not in docs_dir_files or re_compile:
            with open(docs_dir / f"{file.stem}.html", mode="w") as f:
                f.write(render_template(
                    "__main__.html",
                    title=file.stem.split(":")[1],
                    content=markdown.markdown(file.read_text())
                ))


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
