import mistune
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound


def rss_code_block_fixer(code: str) -> str:
    return (
        code.replace("\n", "<br/>")
        .replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
        .replace(" ", "&nbsp;")
    )


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            if info == "jinja2":
                info = "jinja"
            try:
                lexer = get_lexer_by_name(info, stripall=True)
            except ClassNotFound:
                lexer = get_lexer_by_name("text", stripall=True)
            return highlight(code, lexer, HtmlFormatter())
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


class RSSRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        return (
            "<pre><code>" + rss_code_block_fixer(mistune.escape(code)) + "</code></pre>"
        )
