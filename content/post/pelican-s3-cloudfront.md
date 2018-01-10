---
title: Better Pelican Hosting with Amazon S3 and CloudFront
date: 2014-06-21
tags: 
  - python
  - pelican
  - aws
  - meta
  - linode
---

When I first deployed this new static blog it was hosted on [Github Pages](https://pages.github.com/). 
As it turns out thgough, this solution was suboptimal for a few reasons. One problem was that 
since I didn't want to use [Jekyll](http://jekyllrb.com/) I had to check the compiled site into the master
branch, and have a separate `src` branch for the source. But the primary issue was that I like using an apex
domain (i.e. without the "www."). I finally found a nice short domain that I like (pmac.io) and I don't want
to have to shove anything else on the front of it. But if you use an apex domain with github pages it is
[painfully slow](http://instantclick.io/github-pages-and-apex-domains).

So... what to do? Use Amazon S3 of course! I found an [excellent blog post](http://sylvain.durand.tf/static-website-with-cloudfront/) on how best to accomplish it,
but it was specific to Jekyll so I still had to do some more setup. So I thought I'd make notes about those changes here so I'll remember
and hopefully help some other poor micro-optimizing soul out there.

First of all, check out how I use `s3cmd` in [my Makefile](https://github.com/pmclanahan/pmac.io/blob/e65aacf1fd2d05552ddcf7582d04f6456e25f828/Makefile#L85-L87). This, in combination with the [Pelican assets plugin](https://github.com/getpelican/pelican-plugins/tree/master/assets) that bundles, minifies, and gzips my CSS and JS will get you some screaming fast static assets. You have to be aware of some tweaks to settings for the specific paths I used, but it works well for me. I also wrote a [new gzip filter](https://github.com/pmclanahan/pmac.io/blob/e65aacf1fd2d05552ddcf7582d04f6456e25f828/asset_filters.py) for [webassets](https://github.com/miracle2k/webassets) because webassets is dropping their's, and because their's wasn't fully determined by the content, so the file hash was different for every run and thus ruined my very long cache times.

## Conclusion

Even with the awesomeness of this setup, I'm strongly considering just hosting it on [Linode](https://www.linode.com/?r=d069f8df6df96b5407f86bbc2dde1424435ba75c) (referral link).

1. I already have a server at Linode.
2. Doing all of the gzip and cache header stuff would be much easier.
3. Even as little as AWS costs for this, it's more expensive than using a server I already have.
4. I could use a git repo on the server and have it build on push.
5. I could easily run a service to listen for github webhooks to rebuild on push to github.

If I do this I'll be sure to metablog about it and let y'all know how it goes.
