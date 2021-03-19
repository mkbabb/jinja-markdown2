# jinja-markdown2

Inspired by the original [jinja-markdown](https://github.com/jpsca/jinja-markdown).

Uses `jinja2` + `markdown2` to render markdown code _after_ jinja's templating magic
(variable interpolation, etc.) is done. Critical difference between the naive:

    Markdown ->  HTML -> Jinja

Notice, the above processes the markdown _first_ and jinja templating _last_. Whilst
this approach technically works, it results in a myriad of problems with the resultant
HTML that markdown2 formulates.

The flow is then:

    HTML -> Jinja -> Markdown

## Usage

Python:

```python
...
from jinja_markdown2 import MarkdownExtension

jinja_env = ...
jinja_env.add_extension(MarkdownExtension)
...
```

Markdown:

```html
{% markdown %}

## Hello {{ world_name }}

{% endmarkdown %}
```
