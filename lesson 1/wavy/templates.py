from jinja2 import Template
import os


def render_template(template_name, folder='templates', **kwargs):
    filepath = os.path.join(folder, template_name)
    with open(filepath, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
