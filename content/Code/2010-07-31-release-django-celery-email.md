Title: Release: Django Celery Email
Date: 2010-07-31 18:16
Tags: celery, django, django-celery-email, release, python
Alias: post/885869589/release-django-celery-email/index.html

I just released my first [Django](http://djangoproject.com) reusable app. [django-celery-email](http://pypi.python.org/pypi/django-celery-email) is an email backend for Django 1.2+ that uses the amazing [Celery](http://celeryproject.org) to process sending the emails out-of-band. If you're a Python developer and have ever wanted to use a queue to send information to separate processes that will in turn do your bidding and give back to you what you need, then Celery is probably what you want, plus more amazing features that you haven't thought of yet, but that you desperately need. We use Celery at work, and it's been invaluable. If you need it, or are already using it, you might as well move the processing of the email your app sends to a queue as well.

The project is open source (BSD licensed) and can be acquired from PyPI via the link above. It's being developed at [my BitBucket account](http://bitbucket.org/pmclanahan/django-celery-email), so please stop by, check it out, and file a ticket if you find anything lacking or incorrect.
