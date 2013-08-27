import logging
import os
import sys

from jinja2 import Environment, FileSystemLoader
from pelican import signals

logger = logging.getLogger(__name__)

this_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(this_dir))
TEMPLATE = env.get_template('alias.html')

ALIASES = []


def find_alias(content):
    if hasattr(content, 'alias'):
        ALIASES.append(content)


def write_aliases(pelican):
    for content in ALIASES:
        url = '/'.join([content.settings['SITEURL'], content.url])
        html = TEMPLATE.render(content_url=url)
        path = os.path.join(pelican.output_path, content.alias)
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            # likely the dir already exists
            pass
        try:
            with open(path, 'w') as f:
                f.write(html)
        except IOError as e:
            logger.exception('Could not write alias: %s' % content.alias)


def register():
    signals.content_object_init.connect(find_alias)
    signals.finalized.connect(write_aliases)
