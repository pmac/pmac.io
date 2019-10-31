---
title: "The Lounge on Dokku"
date: 2019-10-31T13:44:43-04:00
tags:
  - mozilla
  - docker
  - the-lounge
  - irc
  - dokku
---

Mozilla has hosted an enterprise instance of [IRCCloud][] for several years now, and it's been a great client to use with our IRC network. IRCCloud has deprecated their enterprise product and so Mozilla recently decommissioned our instance. I then saw several colleagues praising [The Lounge][] as a good self-hosted alternative. I became even more interested when I saw that the project maintains a [docker image distribution][] of their releases. I now have an instance running and I'm using irc.mozilla.org via this client and I agree with my colleagues: it's a decent replacement.

<!--more-->

I'm running this on a [Linode][] I have that I use for some personal projects via [Dokku][], complete with an SSL cert from Let's Encrypt! For those interested in replicating this setup, here's what I did:

## Dokku

If you don't already know, the tl;dr for Dokku is that it's an easy way to take a [VM running one of the supported flavors of Linux](http://dokku.viewdocs.io/dokku/getting-started/installation/), and turn it into a Heroku-like hosting platform. It comes complete with a plugin system that allows you to easily spin up a database, memcache, redis, etc., and hook it to your app via simple commands. Most importantly for this it manages an Nginx proxy that handles mapping domains (or app-name subdomains of a primary domain) to running apps.

Dokku supports pretty much everything we need out-of-the-box, so it was just a matter of stringing together the right commands. I'll list them here and explain what's happening:

## Installing The Lounge

Assuming you have Dokku installed and a wildcard DNS entry for a domain you own pointed to your server, we can start by creating a new Dokku app.

```bash
$ dokku apps:create lounge
-----> Creating lounge... done
```

### Persistent Storage

The next thing we'll want is a place to store persistent data (settings and logs) for the app. Dokku recommends using the `/var/lib/dokku/data/storage` directory, which it created during install. Then we use the [Dokku storage][] commands to add this mount to the app config:

```bash
$ mkdir /var/lib/dokku/data/storage/lounge
$ dokku storage:mount lounge "/var/lib/dokku/data/storage/lounge:/var/opt/thelounge"
```

> Note: `/var/opt/thelounge` is the directory that the app uses within the container by default

### The Docker Image

Next we'll need to pull down the docker image for The Lounge. Dokku requires that the images it deploys be tagged with a specific naming convention, so the way to [deploy an existing image][] via the docker hub is to simply pull it and tag it:

```bash
$ docker pull thelounge/thelounge:3.3.0-alpine
$ docker tag !$ dokku/lounge:v1
```

A few points about the above commands:

1. I used the version-specific tag for the image just to be explicit. It's fine to use `:latest` here if you'd rather.
2. The `!$` in the 2nd command is a bash feature that is replaced with the last part of the previous command, so the docker image name in this case.
3. You must use a versioned tag for dokku to deploy it, it will not use `:latest`

### Deploy

Once we have our new image pulled and tagged we can deploy:

```bash
$ dokku tags:deploy lounge v1
```

### Ports

The result of this command should be a running instance of The Lounge on your server, but there's a problem. Dokku doesn't automatically hook up your app to port 80 if it sees an `EXPORT` line in the Dockerfile. The official Dockerfile from The Lounge includes `EXPORT 9000`, so Dokku helpfully maps the container's port 9000 to the host port 9000. To fix it so that Nginx serves it properly we have to tell it about this:

```bash
$ dokku proxy:ports-add lounge http:80:9000
$ # and remove the old port
$ dokku proxy:ports-remove lounge http:9000:9000
```

Now you should be able to visit `http://lounge.your-dokku-domain.com` and see the login page \o/

### Let's Encrypt

It should really use TLS encryption though right?! I mean you will be communicating using this thing, and you'll be sending your user credentials; so yes, you should. Thankfully Dokku makes this very easy by providing an official [Let's Encrypt plugin][]. Once you have that installed and configured it's a simple command to add TLS support to any of your Dokku apps:

```bash
$ dokku letsencrypt lounge
``` 

### Users

The last step is to create yourself a user so that you can login to your fancy new The Lounge instance.

```bash
$ docker exec --user node -it lounge.web.1 thelounge add pmac
2019-10-31 17:33:28 [PROMPT] Enter password:
2019-10-31 17:34:11 [PROMPT] Save logs to disk? (yes)
2019-10-31 17:34:13 [INFO] User pmac created.
2019-10-31 17:34:13 [INFO] User file located at /var/opt/thelounge/users/pmac.json.
```

## Conclusion

Hopefully you are now basking in your huge success, you've logged into The Lounge, joined an IRC network or two, and are chatting happily away, and this guide helped you in some way to achieve that. 

Cheers 🍻

[IRCCloud]: https://irccloud.com
[The Lounge]: https://thelounge.chat
[docker image distribution]: https://thelounge.chat/docs/install-and-upgrade#docker
[Linode]: https://linode.com
[Dokku]: http://dokku.viewdocs.io/dokku/
[Dokku storage]: http://dokku.viewdocs.io/dokku/advanced-usage/persistent-storage/
[deploy an existing image]: http://dokku.viewdocs.io/dokku/deployment/methods/images/#deploying-from-a-docker-registry
[Let's Encrypt plugin]: https://github.com/dokku/dokku-letsencrypt
