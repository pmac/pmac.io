title: Better Pelican Hosting with Amazon S3 and CloudFront
tags: python, blog, pelican, aws
status: draft

When I first deployed this new static blog it was hosted on [Github Pages](https://pages.github.com/). 
As it turns out thgough, this solution was suboptimal for a few reasons. One problem was that 
since I didn't want to use [Jekyll](http://jekyllrb.com/) I had to check the compiled site into the master
branch, and have a separate `src` branch for the source. But the primary issue was that I like using an apex
domain (i.e. without the "www."). I finally found a nice short domain that I like (pmac.io) and I don't want
to have to shove anything else on the front of it. But if you use an apex domain with github pages it is
[painfully slow](http://instantclick.io/github-pages-and-apex-domains).

So... what to do? Use Amazon S3 of course! I found an [excellent blog post]() on how best to accomplish it,
but I still had to do some more setup. So I thought I'd make notes about those changes here so I'll remember
and hopefully help some other poor micro-optimizing soul out there.
