Title: Cookies for Django
Tags: python, django
Alias: post/1660050353/cookies-for-django/index.html

Until yesterday I thought the new [messages framework in Django 1.2](http://docs.djangoproject.com/en/1.2/ref/contrib/messages/) was doing things stupidly. I like the [Fallback backend](http://docs.djangoproject.com/en/1.2/ref/contrib/messages/#storage-backends); it uses signed cookies to store the messages that will be displayed to the user. This avoids the DB or cache hits that'd you'd normally get from the old system, as well as those you'd get from using the session for message storage. The Fallback goes further and will use the session if your message is too big for a cookie. Awesome right? My problem was that the messages weren't showing up on the page until the request AFTER the one in which I set the message. I could see nothing I'd done wrong at the time, so I assumed that it was just the way it worked w/ cookies, b/c cookies have to be set in the browser and are only sent back to the server on subsequent requests.

It turns out that this is, of course, **not** the way the messages framework was designed. It will display the messages in the current request, but only if you haven't already called the view, thus rendering the template(s). How could it display the messages if you've rendered the page before adding the messages??!?!!?!?! I was being an idiot. I was trying to set messages in a view decorator, and was doing it after calling the view. That stupid bug took me a LONG time to find. In my defense however, I did have a good reason for having to call the view in my decorator before adding my messages: I needed to set cookies.

In Django, the only way to set your own cookies to be stored on your user's browser is to use the `set_cookie` method on the `HttpResponse` class. This means that you'll need access to the response instance before you can set cookies. To get the response in a decorator you have to call the view. Do you see my predicament?

I thought I'd found the answer in a [post from David Cramer](http://www.davidcramer.net/code/62/set-cookies-without-a-response-in-django.html). He created a Django middleware that would allow you to set cookies using the request object. This, I thought, was perfect and would solve my problem completely. I installed his [django-cookies](https://github.com/dcramer/django-cookies) app, changed my decorator around to use it, and ran the test suite: FAIL. David's code has apparently not been updated in some time, and is not compatible with Django 1.2. So I was left with nothing but the idea that this was a solvable problem. I decided to write my own middleware.

My cookie middleware works pretty much the same as David's, but with a different API. I decided to add methods to the request object itself that exactly mirror the ones on response. [Check out the code](https://gist.github.com/pmclanahan/710480), let me know what you think, and feel free to use it however you like. I plan to package it up as a Django app soon, but I wanted to get it out there in case someone else was having similar troubles.

    #!python
    from types import MethodType

    from django.http import CompatCookie, HttpRequest

    def _set_cookie(self, key, value='', max_age=None, expires=None, path='/',
               domain=None, secure=False):
        self._resp_cookies[key] = value
        self.COOKIES[key] = value
        if max_age is not None:
            self._resp_cookies[key]['max-age'] = max_age
        if expires is not None:
            self._resp_cookies[key]['expires'] = expires
        if path is not None:
            self._resp_cookies[key]['path'] = path
        if domain is not None:
            self._resp_cookies[key]['domain'] = domain
        if secure:
            self._resp_cookies[key]['secure'] = True


    def _delete_cookie(self, key, path='/', domain=None):
        self.set_cookie(key, max_age=0, path=path, domain=domain,
                        expires='Thu, 01-Jan-1970 00:00:00 GMT')
        try:
            del self.COOKIES[key]
        except KeyError:
            pass


    class RequestCookies(object):
        """
        Allows setting and deleting of cookies from requests in exactly the same
        way as responses.

        >>> request.set_cookie('name', 'value')

        The set_cookie and delete_cookie are exactly the same as the ones built
        into the Django HttpResponse class.

        http://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse.set_cookie
        """
        def process_request(self, request):

            request._resp_cookies = CompatCookie()
            request.set_cookie = MethodType(_set_cookie, request, HttpRequest)
            request.delete_cookie = MethodType(_delete_cookie, request, HttpRequest)

        def process_response(self, request, response):
            if hasattr(request, '_resp_cookies') and request._resp_cookies:
                response.cookies.update(request._resp_cookies)

            return response
