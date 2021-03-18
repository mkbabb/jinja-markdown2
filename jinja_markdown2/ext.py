from typing import *

import markdown2
from jinja2.ext import Extension
from jinja2.nodes import CallBlock


class MarkdownExtension(Extension):
    tags = {"markdown"}

    def __init__(
        self,
        environment: Any,
        md_extras: List[str] = [
            "footnotes",
            "markdown-in-html",
            "fenced-code-blocks",
        ],
    ):
        super(MarkdownExtension, self).__init__(environment)
        self.md_extras = set(md_extras)
        self.t_md_extras = set()

    def parse(self, parser) -> CallBlock:
        lineno = next(parser.stream).lineno

        if parser.stream.current.type == "pipe":
            args = parser.parse_tuple(simplified=True)
            names = (
                set((i.name for i in args))
                if isinstance(args, tuple)
                else set([args.name])
            )
            self.t_md_extras = self.md_extras | names
        else:
            self.t_md_extras = {}

        body = parser.parse_statements(["name:endmarkdown"], drop_needle=True)

        return CallBlock(self.call_method("_markdown"), [], [], body).set_lineno(lineno)

    def _markdown(self, caller) -> Text:
        md = markdown2.Markdown(extras=self.t_md_extras)
        text: Text = caller()
        text = textwrap.dedent(text.strip())

        return md.convert(text)
