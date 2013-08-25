import os

from jinja2 import Environment, FileSystemLoader
from pelican import signals


this_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(this_dir))
template = env.get_template('alias.html')

ALIASES = {}


def find_alias(content):
    if hasattr(content, 'alias'):
        url = '/'.join([content.settings['SITEURL'], content.url])
        html = template.render(content_url=url)
        ALIASES[content.alias] = html


def write_aliases(pelican):
    for alias, html in ALIASES.iteritems():
        path = os.path.join(pelican.output_path, alias)
        os.makedirs(os.path.dirname(path))
        with open(path, 'w') as f:
            f.write(html)


def register():
    signals.content_object_init.connect(find_alias)
    signals.finalized.connect(write_aliases)
