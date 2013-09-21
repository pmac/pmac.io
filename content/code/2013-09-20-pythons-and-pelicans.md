title: Pythons, Pelicans, and Posts
tags: python, blog, pelican, release

<img src="|filename|/images/pelicans.jpg" style="float:left;" alt="Pelicans!">
As most web developers are want to do more often than most,
I've changed the tech underlying my blog. My first blog was
a custom PHP beast completely hand-written by me and found at
paulmclanahan.com sometime around 2001. In the time since
I've tried wordpress, blogspot, and tumblr, and moved to
paulm.us and now pmac.io. I've not felt fully
comfortable since relinquishing control of the hosting
and technology of my site. I've also moved from PHP to Python as my
primary programming language of choice. So much so in fact
that I do everything in my power to avoid reading
or writing PHP. I'm truly spoiled by Python and I'm much
happier there. So clearly I needed a blogging platform that is
Python-based so that I can hack on it and not dread
the code, which also means I need to wrest full control of the code
back from my lazy days of hosted platforms (wordpress.com, tumblr, etc.).

I've also grown fond of the idea of a fully static site.
Blogs don't change much (at least not the way I do them). So to the
engineer in me it makes very little sense to have a database and application
server running to dynamically construct HTML for requests. Said HTML should
be generated when I post something new, and only then. This is especially
true now that I've grown fond of the trend of not having comments on
blogs. Comment forms just invite security issues, spam, and anonomyous trolls.
I could have easily added commenting via Disqus or Facebook, but I'm
taking a queue from [a favorite Mozillian of mine](http://blog.seanmartell.com)
and just putting a "respond on twitter" link at the bottom of every post.
This way if you want to berate me, you'll have to at least let me see
your twitter handle, or go to the trouble of creating a burner account.

So, with those decisions made I was faced with the decision of finding a
decent Python-based static site generator or writing one? I had plans to
do the latter. It was to be called
"Trogdor" and it would burninate your village as you published your peasant pages. Lack
of free time delayed those plans enough that I found a great version of what
I wanted to do already existed. It's called [Pelican][] and it uses all the
things I wanted. It's quite hackable (has a [nice plugin system][plugins]), it uses
[Jinja2][] for templating, you can write posts in [Markdown][] or [reStructuredText][],
and the post metadata is contained in the post files themselves.

[Pelican]: http://getpelican.com/
[plugins]: http://docs.getpelican.com/en/latest/plugins.html
[Jinja2]: http://jinja.pocoo.org/
[Markdown]: http://daringfireball.net/projects/markdown/
[reStructuredText]: http://docutils.sourceforge.net/rst.html

Once all that was decided it was a simple matter of finding a theme and hacking
it to bits. Pelican has the great advantage of a burgeoning community forming
around it, so there are [several plugins](https://crate.io/?has_releases=on&q=pelican) and templates out there to get you started.
I chose [Sundown][] and am pretty happy with it. I'll keep tweaking and may change
it entirely, but [Pelican][] makes that very easy.

Because I have switched around a lot I do have some post history. For various reasons
I ditched all my posts when I switched to Tumblr. But I did want to bring the tumblrs
with me to the new system. This new platform allows me to have post urls I like, unlike tumblr.
But I don't like link-rot, so I needed a way to redirect the old URLs to the new home
for the post. The wrinkle is that I wanted to host the site on [Github Pages][] which
has no server-side redirect capabilities. So I wrote my own plugin that would allow
you to set an "alias" on your posts that would cause Pelican to output html files at
the old URL locations that contained the proper meta-refresh tag to redirect the user
to the new URL, and tell Google that the post has moved when next they spider. Only
after I had it working of course did I find [pelican-alias][], which does all those
things, only better, and to which I've switched.

[Sundown]: https://github.com/keningle/pelican-sundown
[Github Pages]: http://pages.github.com/
[pelican-alias]: https://github.com/Nitron/pelican-alias
[pelican-link-bugs]: https://github.com/pmclanahan/pelican-link-bugs

I did have one more thing I wanted though, and could not find anything existing to do it.
I wanted to be able to easily link to bugs in Mozilla's Bugzilla, and issues and pull-requests on
Github. So I wrote and released [pelican-link-bugs][]. It allows you to easily link to
things like bug 765645, or PR mozilla/bedrock#1127. It's also very easy (if you know
regular expressions) to add your own search-and-replace-with-link patterns.

So there you have it. The blog is moved, the code is new, and the first new post is
all about all of that. If you got this far I'm quite impressed. Thanks for taking the time.

[Pelican photo](http://www.flickr.com/photos/bertknot/8121224533) by Flickr user bertknot.
