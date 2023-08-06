from datetime import datetime
from pathlib import Path

import mistune
from flask import Flask, render_template
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
from pytz import timezone


def pytz_datetime_str(ltz: str = "Europe/London", mask: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
    local_tz = timezone(ltz)
    return datetime.strptime(datetime.now(local_tz).strftime(mask), mask).strftime(mask)


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
docs_dir = cwd / "docs"
markdown_dir = cwd / "markdown"
index_html = docs_dir / "index.html"
index_xml = docs_dir / "index.xml"


def get_docs_files() -> list:
    _ = []
    for f in docs_dir.glob("*.html"):
        if f.stem == "index":
            continue
        _.append(f.stem)

    return _


def compiler(re_compile=False):
    docs_dir_files = get_docs_files()
    markdown_dir_files = markdown_dir.glob("*.md")

    pages = {}

    if re_compile:
        for file in docs_dir_files:
            (docs_dir / f"{file}.html").unlink()

    for file in markdown_dir_files:
        title = "Untitled"
        description = "No description"
        date = "No date"

        if file.stem not in docs_dir_files or re_compile:
            raw_markdown = file.read_text()
            split_markdown = raw_markdown.split("::::")
            raw_info = split_markdown[0].strip().replace(
                "\n", "").split(",")
            for info_item in raw_info:
                if info_item.startswith("title="):
                    title = info_item.split('"')[1]
                elif info_item.startswith("description="):
                    description = info_item.split('"')[1]
                elif info_item.startswith("date="):
                    raw_date = info_item.split('"')
                    date = datetime.strftime(
                        datetime.strptime(raw_date[1], "%Y-%m-%d"), "%a, %d %b %Y")

            content = split_markdown[1]
            markdown = mistune.Markdown(renderer=HighlightRenderer())

            with open(docs_dir / f"{file.stem}.html", mode="w") as html_file:
                html_file.write(render_template(
                    "__main__.html",
                    title=title,
                    description=description,
                    date=date,
                    content=markdown(content)
                ))

            pages[f"{file.stem}.html"] = {
                "title": title,
                "description": description,
                "date": date,
                "content": markdown(content)
            }

    index_html.write_text(
        render_template(
            "index.html",
            pages=pages
        )
    )

    index_xml.write_text(
        render_template(
            "index.xml",
            build_date=pytz_datetime_str(mask="%a, %d %b %Y"),
            pages=pages
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

    @app.cli.command("add-page")
    def add_page():
        title = input("Title: ")
        filename = f"{pytz_datetime_str(mask='%Y-%m-%d')}:{title.lower().replace(' ', '-') or 'untitled'}.md"
        with open(markdown_dir / filename, mode="w") as file:
            file.write(
                """\
title="{title}"
description="Description"
date="{date}"

::::

# Title
""".format(title=title or "Untitled", date=pytz_datetime_str(mask="%Y-%m-%d"))
            )

    return app
