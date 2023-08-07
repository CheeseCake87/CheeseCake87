import re
from datetime import datetime
from pathlib import Path

import mistune
from flask import Flask, render_template
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
from pytz import timezone

local_tz = timezone("Europe/London")
cwd = Path(__file__).parent
docs_dir = cwd / "docs"
markdown_dir = cwd / "markdown"
index_html = docs_dir / "index.html"
index_xml = docs_dir / "index.xml"


def switch_date(content, new_date):
    pattern = re.compile(r'date="[A-Za-z]+"', re.IGNORECASE)
    return pattern.sub(f'date="{new_date}"', content)


def pytz_datetime() -> datetime:
    return datetime.now(local_tz)


def pytz_datetime_str(mask: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
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


def get_docs_files() -> list:
    _ = []
    for f in docs_dir.glob("*.html"):
        if f.stem == "index":
            continue
        _.append(f.stem)

    return _


def compiler():
    docs_dir_files = get_docs_files()
    markdown_dir_files = markdown_dir.glob("*.md")

    html_pages = dict()
    xml_pages = dict()

    for file in docs_dir_files:
        (docs_dir / f"{file}.html").unlink()

    for file in markdown_dir_files:
        title = "Untitled"
        description = "No description"
        date = "No date"

        raw_markdown = file.read_text()
        split_markdown = raw_markdown.split("::::")
        raw_info = split_markdown[0].strip().replace(
            "\n", "").split(",")

        content = split_markdown[1]
        html_content = mistune.create_markdown(renderer=HighlightRenderer())
        xml_content = mistune.create_markdown()

        for info_item in raw_info:
            if info_item.startswith("title="):
                title = info_item.split('"')[1]
            elif info_item.startswith("description="):
                description = info_item.split('"')[1]
            elif info_item.startswith("date="):
                raw_date = info_item.split('"')
                try:
                    date = datetime.strftime(
                        datetime.strptime(
                            raw_date[1],
                            "%Y-%m-%d %H:%M:%S %z"
                        ), "%a, %d %b %Y %H:%M:%S %z")
                except ValueError:
                    date_now = pytz_datetime()
                    date = date_now.strftime("%a, %d %b %Y %H:%M:%S %z")

                    with open(file, mode="w") as f:
                        f.write(switch_date(raw_markdown, date_now.strftime("%Y-%m-%d %H:%M:%S %z")))

        if "0000-00-00" in file.stem:
            raw_filename = file.stem.replace("0000-00-00", pytz_datetime_str(mask="%Y-%m-%d"))
            split_filename = raw_filename.split("_")
            filename = "_".join([split_filename[0], title.lower().replace(" ", "-")])
        else:
            split_filename = file.stem.split("_")
            filename = "_".join([split_filename[0], title.lower().replace(" ", "-")])

        file.rename(markdown_dir / f"{filename}.md")

        with open(docs_dir / f"{filename}.html", mode="w") as html_file:
            html_file.write(render_template(
                "__main__.html",
                title=title,
                description=description,
                date=date,
                content=html_content(content)
            ))

        html_pages[f"{filename}.html"] = {
            "title": title,
            "description": description,
            "date": date,
            "content": html_content(content)
        }

        this_xml = xml_content(content)
        pre_tag_pattern = re.compile(r"(?:<pre>)(.*)(?:<\/pre>)", re.IGNORECASE | re.DOTALL)
        pre_tag_matches = pre_tag_pattern.findall(this_xml)

        for match in pre_tag_matches:
            this_xml = re.sub('\s+', lambda x: ']]>' + '&32;' * len(x[0]) + '<![CDATA[', match)

        xml_pages[f"{filename}.html"] = {
            "title": title,
            "description": description,
            "date": date,
            "content": f"<![CDATA["
                       "<p>Having trouble viewing the content below? "
                       f"<a href='https://thecodingside.quest/{filename}.html target='_blank'>"
                       "View original post here</a></p>"
                       f"{this_xml}"
                       "]]>"
        }

    html_pages_sorted = {k: v for k, v in sorted(html_pages.items(), reverse=True)}
    xml_pages_sorted = {k: v for k, v in sorted(xml_pages.items(), reverse=True)}

    index_html.write_text(
        render_template(
            "index.html",
            pages=html_pages_sorted
        )
    )

    index_xml.write_text(
        render_template(
            "index.xml",
            build_date=pytz_datetime_str(mask="%a, %d %b %Y %H:%M:%S %z"),
            pages=xml_pages_sorted
        )
    )


def create_app():
    app = Flask(__name__)
    app.static_folder = "static"
    app.template_folder = "templates"

    @app.cli.command("compile")
    def compile_site():
        compiler()

    @app.cli.command("add-page")
    def add_page():
        title = input("Title: ")
        filename = f"0000-00-00_{title.lower().replace(' ', '-') or 'untitled'}.md"
        with open(markdown_dir / filename, mode="w") as file:
            file.write(
                """\
title="{title}",
description="Description",
date="{date}",

::::

start here...
""".format(title=title.title() or "Untitled", date="set-on-compile"))

    return app
