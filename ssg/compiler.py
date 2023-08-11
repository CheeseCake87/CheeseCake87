import re
from pathlib import Path

import mistune
from flask import render_template

from ssg.exceptions import NoPostDefinition
from ssg.helpers import (
    get_docs_files,
    excessive_br_cleanup,
    pytz_dt_now_str, pytz_dt_now,
    pytz_dt_str_to_dt,
    post_date
)
from ssg.render_engines import HighlightRenderer, RSSRenderer


def _find_post_meta(split_markdown: str) -> tuple:
    publish_ptn = re.compile(r'Publish =(.*?)\n', re.IGNORECASE)
    date_ptn = re.compile(r'Date =(.*?)\n', re.IGNORECASE)
    title_ptn = re.compile(r'Title =(.*?)\n', re.IGNORECASE)
    description_ptn = re.compile(r'Description =(.*?)\n', re.IGNORECASE)

    try:
        publish = publish_ptn.findall(split_markdown)[0].strip()
    except (ValueError, IndexError, TypeError) as _:
        publish = False

    try:
        date = date_ptn.findall(split_markdown)[0].strip()
    except (ValueError, IndexError, TypeError) as _:
        date = "[Unable to find Date]"

    try:
        title = title_ptn.findall(split_markdown)[0].strip()
    except (ValueError, IndexError, TypeError) as _:
        title = "[Unable to find Title]"

    try:
        description = description_ptn.findall(split_markdown)[0].strip()
    except (ValueError, IndexError, TypeError) as _:
        description = "[Unable to find Description]"

    return (
        True if isinstance(publish, str) and publish.lower() == "true" else False,
        date,
        title,
        description,
    )


def _raw_markdown_processor(raw_markdown: str) -> tuple[bool, str, str, str, str]:
    """
    :param raw_markdown: The raw markdown to process
    :return: publish: bool, date: str, title: str, description: str, post: str
    """
    if not raw_markdown.startswith("```"):
        raise NoPostDefinition

    split_md = raw_markdown.split("```")[1:]
    raw_meta = split_md[0]

    publish, date, title, description = _find_post_meta(raw_meta)

    try:
        post = "```".join(split_md[1:])
    except (IndexError, TypeError, ValueError) as _:
        post = "[Unable to find Post]"

    return publish, date, title, description, post


def replace_post_date(content: str, new_date: str) -> str:
    date_ptn = re.compile(r'Date =(.*?)\n', re.IGNORECASE)
    return content.replace(
        date_ptn.findall(content)[0],
        f"Date = {new_date}"
    )


def compiler(cwd: Path, recompile: bool = False):
    docs_dir = cwd / "docs"
    markdown_dir = cwd / "markdown"
    index_html = docs_dir / "index.html"
    index_xml = docs_dir / "index.xml"

    docs_dir_files = get_docs_files(docs_dir)
    markdown_dir_files = markdown_dir.glob("*.md")

    html_pages = dict()
    xml_pages = dict()

    if recompile:
        for file in docs_dir_files:
            (docs_dir / f"{file}.html").unlink()

    for file in markdown_dir_files:
        raw_markdown = file.read_text()
        publish, date, title, description, post = _raw_markdown_processor(raw_markdown)

        html_engine = mistune.create_markdown(renderer=HighlightRenderer())
        xml_engine = mistune.create_markdown(renderer=RSSRenderer())

        if publish:
            try:
                dt_date = pytz_dt_str_to_dt(date)
            except ValueError:
                dt_date = pytz_dt_now()

            new_filename = f"{dt_date.strftime('%Y-%m-%d')}_{title.replace(' ', '-').lower()}"

            with open(docs_dir / f"{new_filename}.html", mode="w") as html_file:
                html_file.write(render_template(
                    "__main__.html",
                    title=title,
                    description=description,
                    date=post_date(dt_date),
                    content=html_engine(post)
                ))

            html_pages[f"{new_filename}.html"] = {
                "title": title,
                "description": description,
                "date": post_date(dt_date),
                "content": html_engine(post)
            }

            xml_pages[f"{new_filename}.html"] = {
                "title": title,
                "description": description,
                "date": post_date(dt_date),
                "content": "<![CDATA["
                           "<p>Having trouble viewing the content below? "
                           f'<a href="https://thecodingside.quest/{new_filename}.html">'
                           "View original post here</a></p>"
                           f"{excessive_br_cleanup(xml_engine(post))}"
                           "]]>"
            }
        else:
            new_filename = f"0000-00-00_{title.replace(' ', '-').lower()}"

        file.write_text(replace_post_date(file.read_text(), "2021-08-01 00:00:00 +0000"))
        file.rename(markdown_dir / f"{new_filename}.md")

    # sort pages by filename
    html_pages_sorted = {k: v for k, v in sorted(html_pages.items(), reverse=True)}
    xml_pages_sorted = {k: v for k, v in sorted(xml_pages.items(), reverse=True)}

    # write main index.html
    index_html.write_text(
        render_template(
            "index.html",
            pages=html_pages_sorted
        )
    )

    # write main index.xml
    index_xml.write_text(
        render_template(
            "index.xml",
            build_date=pytz_dt_now_str(mask="%a, %d %b %Y %H:%M:%S %z"),
            pages=xml_pages_sorted
        )
    )
