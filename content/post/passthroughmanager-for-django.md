---
title: PassThroughManager for Django
date: 2011-03-08
tags: 
  - python
  - django
aliases: /post/3717466639/passthroughmanager-for-django/
---

**Update 3/30/2011:** This has been merged into [Django-model-utils](https://bitbucket.org/carljm/django-model-utils/) (Thanks to [Carl Meyer](https://bitbucket.org/carljm)). There is a ton of useful stuff in that package. You should really be using it. I am.

Django's built-in Model Manager and QuerySet classes include plenty of useful methods. But often you'll want more. Django makes it very easy to subclass these built-ins to add your own properties and methods. However, more often than not, you'll want the same methods to exist on your new manager and queryset. This is also easy, but requires a lot of boilerplate code to accomplish.

I found a project that helps with this. [Django-model-utils](https://bitbucket.org/carljm/django-model-utils/) includes a number of helpful methods and classes for most Django projects. I tried using the **manager_from** method from this project to solve the problem I mentioned above. It worked for the simple cases, but my tests started failing for a more complex one. It turns out that the method employed in **manager_from** causes problems when pickling the resulting querysets. Django querysets are designed to be picklable, so this was troubling. It seems to stem from the fact that the actual queryset classes produced by this method are dynamic, and thus don't exist in any importable way. The pickle and unpickle methods need to be able to import the queryset class however.

To solve this problem I wrote a class called **PassThroughManager**. If you have a simple set of methods you want to exist on a manager and queryset, you can do the following:

```python
class PostQuerySet(QuerySet):
    def enabled(self):
        return self.filter(disabled=False)

class Post(models.Model):
    objects = PassThroughManager(PostQuerySet)
```

You'd then be able to use both **Post.objects.enabled()** and **Post.objects.filter(other='stuff').enabled()**. If you had other methods you wanted to add to your manager but not your queryset, just subclass PassThroughManager and you can do anything you want. This method has the advantage of maintaining picklability, and is a bit more readable in my opinion. [Grab the code and try it for yourself](https://gist.github.com/pmclanahan/859473). Feedback is most welcome and encouraged.

```python
from django.db.models.manager import Manager


class PassThroughManager(Manager):
    '''
    Inherit from this Manager to enable you to call any methods from your
    custom QuerySet class from your manager. Simply define your QuerySet
    class, and return an instance of it from your manager's `get_query_set`
    method.

    Alternately, if you don't need any extra methods on your manager that
    aren't on your QuerySet, then just pass your QuerySet class to this
    class' constructer.

    class PostQuerySet(QuerySet):
        def enabled(self):
            return self.filter(disabled=False)

    class Post(models.Model):
        objects = PassThroughManager(PostQuerySet)
    '''
    # pickling causes recursion errors
    _deny_methods = ['__getstate__', '__setstate__']

    def __init__(self, queryset_cls=None):
        self._queryset_cls = queryset_cls
        super(PassThroughManager, self).__init__()

    def __getattr__(self, name):
        if name in self._deny_methods:
            raise AttributeError(name)
        return getattr(self.get_query_set(), name)

    def get_query_set(self):
        if self._queryset_cls is not None:
            return self._queryset_cls(self.model, using=self._db)
        return super(PassThroughManager, self).get_query_set()
```
