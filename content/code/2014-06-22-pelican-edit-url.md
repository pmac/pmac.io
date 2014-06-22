title: Pelican Edit Links
tags: pelican, python, release

I wanted to add "Edit on Github" links to every page of my blog. I couldn't find a plugin that does this, so I wrote one. Introducing [Pelican Edit URL](https://github.com/pmclanahan/pelican-edit-url). It's a plugin for [Pelican](http://getpelican.com) that adds an `edit_url` property to article and page objects. This allows you to do things like:

```jinja2
<a href="{{ article.edit_url }}">edit on github</a>
```

I use this to link to the page markdown source in github, but the link generated is fully customizable. Just set `EDIT_CONTENT_URL` to whatever you want, and include `{file_path}` in it where the path to the source file needs to go. For example:

```python
EDIT_CONTENT_URL = 'https://github.com/pmclanahan/pmac.io/blob/master/{file_path}'
```

You can see it in action at the bottom of this and most other pages on this site. Let me know if this helps you out or if you have suggestions for improvement. You can get the source for the plugin at the link above, or install from PyPI using pip:

```bash
pip install pelican-edit-url
```