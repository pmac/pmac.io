---
title: Slicehost Dynamic DNS
date: 2010-08-17
tags: 
  - python
  - slicehost
  - dns
aliases: /post/967252453/slicehost-dynamic-dns/
---

One of the best things about [Slicehost](http://slicehost.net) is their DNS service. They allow you to host and easily maintain any number of zones you want, even ones that aren't hosted on a slice. They also provide an excellent RESTful API for automatically modifying these zones and records. This came to mind recently when my free Dynamic DNS host ([EveryDNS](http://everydns.net)) was sold to [Dyn, Inc.](http://dyn.com/). I decided it was time to grow up and move my dynamic DNS needs to a service for which I was paying. I looked into Dyn's offerings, but their Custom DNS service is only for a single domain, and seems pricey for what you get. I know a lot of that has to do with their global distribution and uptime guarantees, but I don't need that stuff.

So, I began writing a little Python CGI that could act as something my home router could use as a Dynamic DNS endpoint. I use [Tomato](http://www.polarcloud.com/tomato) on my Buffalo WHR-HP-G54, and it supports using a custom URL for this purpose. It was surprisingly easy to get this working. I have no idea if anyone else has a similar setup, uses Slicehost, and needs Dynamic DNS, but if you're out there, I've released the code for my little project on [Bitbucket](http://bitbucket.org/). It's called, not surprisingly, [slicehost-dynamic-dns](http://bitbucket.org/pmclanahan/slicehost-dynamic-dns/src). Grab it, clone it, fork it, use it, whatever you want. It's BSD licensed for your pleasure. Please drop me a line if you use it, and if you need a feature or find a bug, throw a ticket in the tracker on the Bitbucket project. You could also fork it, fix it, and send a pull request. That'd be cool too :)
