import jinja2
from jinja_markdown2 import MarkdownExtension

template_path = "tests/template.md"

jinja_env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader("."))
jinja_env.add_extension(MarkdownExtension)

template = jinja_env.get_template(template_path)

template_vars = dict(canto_number="IV")

html = template.render(**template_vars)

with open("tests/test.html", "w") as file:
    file.write(html)
