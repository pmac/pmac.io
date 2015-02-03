title: The State of Mozilla.org
tags: mozilla, bedrock

I'm starting a new blog post series. I'm calling it, as the title of this post suggests,
"The State of Mozilla.org", which is possibly confusing, but I think funny. So we'll try
it for now. The purpose of this is to have a bi-weekly log of what's been happening with
the "www.mozilla.org" site both technically and from a contribution standpoint. I want to
do a better job of being transparent about what's been happening and who's been doing it.
This is all inspired by my friend [willkg's similar series about Input][input], which I think is great.

So, to that end, I'm starting with the beginning of the year, and then I'll be attempting to do this
every two weeks from there mostly to keep this managable. These posts will include the log from git
in the bedrock repo, any particularly interesting bugs, and calls out for new or particularly great contributors.

## State of Mozilla.org for February 2nd, 2015

A lot has been happening on the backend. We're in the process of upgrading Python to 2.7, and
the dev and demo servers have already been done (HOORAY! Thanks [jakem][]!).
We've also [upgraded Django to the 1.6 branch][django-1.6] (though this was a bit more than 2 weeks ago.
Once Python 2.7 fully lands we'll start the move to Django 1.7 and all it's sweet, sweet improvements.
I've made a [wiki page of the process][bedrock-doc] that I'm continuing to tweak. Feedback welcome of course :)

On the frontend we launched the [CES landing page][fxos-tv] about the FxOS powered TVs (DO WANT!),
and we built and launched the [Firefox Hello First-Time-Experience][fx-hello] page. These major
product and feature release pages don't seem to be slowing, so expect even more soon.

### New Contributors ###

I'd like to particularly thank [Utkarsh Bansal](https://github.com/utkbansal) for their first contributons
to bedrock this month. Utkarsh has now closed 2 bugs! Huge help. Thanks a lot!

Another contributor I'd like to call out for his continuation of excellent and copious work, and whose name you'll
see in these git logs quite often, is [Kohei Yoshino](https://github.com/kyoshino). He's fixed so many bugs it'd be
silly for me to list them. Thanks again Kohei, you're truly a friend of [The Dino][dino]!

### 4 Week Git Log

We'll do two weeks from now on, but to get started let's start with the new year. These are the actual
changes made to do the things mentioned above. Feel free to check our work and [send us a PR][bedrock-prs] if we've
been silly in our haste.

> <pre>
> (bedrock) ± [git log --no-merges --since=2015-01-01 --pretty=format:"%h - %ad - %an - %s" --date=short](https://github.com/mozilla/bedrock/compare/1872bd7...2c5e49c)
> [2c5e49c](https://github.com/mozilla/bedrock/commit/2c5e49c) - 2015-02-02 - Bansal Utkarsh - Fixes Bug 1062441 - Add anchors
> [25a8afa](https://github.com/mozilla/bedrock/commit/25a8afa) - 2015-02-02 - Francesco Lodolo (:flod) - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [158cd6c](https://github.com/mozilla/bedrock/commit/158cd6c) - 2015-01-30 - Gervase Markham - Scope CSS to avoid adding number to mozilla header.
> [d71cc75](https://github.com/mozilla/bedrock/commit/d71cc75) - 2015-01-26 - TheoChevalier - Bug 1125971 - Fixing quotes on /fr/privacy/tips/ and removing extra space before the closing quotation mark
> [4b2556d](https://github.com/mozilla/bedrock/commit/4b2556d) - 2015-01-30 - Bansal Utkarsh - Fixes Bug 1122937 - Errornous hex color value
> [11cdcd1](https://github.com/mozilla/bedrock/commit/11cdcd1) - 2015-01-29 - Paul McLanahan - Upgrade django-extensions to 1.4.9.
> [d87c554](https://github.com/mozilla/bedrock/commit/d87c554) - 2015-01-28 - Cory Price - [fix bug 1127120] Add GA events for download/update buttons
> [07bf7a7](https://github.com/mozilla/bedrock/commit/07bf7a7) - 2015-01-28 - Kohei Yoshino - Fix Bug 1126915 - update links on desktop pages to new privacy blog post
> [65a60fe](https://github.com/mozilla/bedrock/commit/65a60fe) - 2015-01-27 - Steven Garrity - Bug 1109318 Update sharing tile image
> [2c24912](https://github.com/mozilla/bedrock/commit/2c24912) - 2015-01-28 - Alex Gibson - [fix bug 1125623] The favicon is not transparent on mozilla.org
> [d4c2f16](https://github.com/mozilla/bedrock/commit/d4c2f16) - 2015-01-27 - Kohei Yoshino - Fix Bug 1125011 - Non-existent security advisory translations are not redirected to en-US
> [2b43710](https://github.com/mozilla/bedrock/commit/2b43710) - 2015-01-27 - Craig Cook - bug 1112324 - update privacy shield image
> [0957843](https://github.com/mozilla/bedrock/commit/0957843) - 2015-01-27 - Kohei Yoshino - Fix Bug 1097785 - Legal-docs-based pages should not rely on active tags in .lang files
> [a83d23a](https://github.com/mozilla/bedrock/commit/a83d23a) - 2015-01-27 - Steven Garrity - Bug 1109318 Update GA campaign for Privay Day
> [bc20db6](https://github.com/mozilla/bedrock/commit/bc20db6) - 2015-01-26 - Jon Petto - Add share widget to Hello product page. Bug 1119849.
> [84a009c](https://github.com/mozilla/bedrock/commit/84a009c) - 2015-01-26 - Jon Petto - Update Hello product page og:image. Bug 1125346.
> [e979d48](https://github.com/mozilla/bedrock/commit/e979d48) - 2015-01-07 - Steven Garrity - Bug 1109318 Privacy Day landing page for 2015
> [2bee1fd](https://github.com/mozilla/bedrock/commit/2bee1fd) - 2015-01-26 - Kohei Yoshino - Fix Bug 1125166 - Some mozilla.org-sites consider 31.4ESR to be out of date
> [680cbf2](https://github.com/mozilla/bedrock/commit/680cbf2) - 2015-01-23 - Kohei Yoshino - Fix Bug 1123977 - www.mozilla.org contribute - error message on the category list could be displayed at a confusing position
> [81df26a](https://github.com/mozilla/bedrock/commit/81df26a) - 2015-01-11 - mermi - Fixes for RTL community events list
> [1835cf3](https://github.com/mozilla/bedrock/commit/1835cf3) - 2015-01-22 - Alex Gibson - [fix bug 1124628] Remove pinned tab APIs from UITour lib & docs
> [0777b56](https://github.com/mozilla/bedrock/commit/0777b56) - 2015-01-20 - Craig Cook - Bug 1112324 - updates to privacy day home promo
> [ccbe4d6](https://github.com/mozilla/bedrock/commit/ccbe4d6) - 2015-01-16 - Alex Gibson - [fix bug 1122519] Remove UA detection and use feature detect for CSS line animations
> [224e1da](https://github.com/mozilla/bedrock/commit/224e1da) - 2015-01-22 - Gervase Markham - Add new LESS file for page, and use CSS counters for heading numbering.
> [603242c](https://github.com/mozilla/bedrock/commit/603242c) - 2015-01-22 - Francesco Lodolo (:flod) - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [ee80fd1](https://github.com/mozilla/bedrock/commit/ee80fd1) - 2015-01-22 - Alex Gibson - [fix bug 1124570] Remove delay showing home promo's for smaller screens
> [858e9a8](https://github.com/mozilla/bedrock/commit/858e9a8) - 2015-01-21 - Josh Mize - peepin compiled requirments
> [f8f4a7e](https://github.com/mozilla/bedrock/commit/f8f4a7e) - 2015-01-21 - Jon Petto - Ignore ESR when checking isFirefoxUpToDate. Bug 1122154.
> [91efc84](https://github.com/mozilla/bedrock/commit/91efc84) - 2015-01-19 - Jon Petto - Add TEF logo to intro. Bug 1119435.
> [9a1c22e](https://github.com/mozilla/bedrock/commit/9a1c22e) - 2015-01-19 - Kohei Yoshino - Fix Bug 1123382 - Add a few more locales to the canonical locale list
> [fa10834](https://github.com/mozilla/bedrock/commit/fa10834) - 2015-01-13 - Craig Cook - Bug 1112324 - Privacy Day home page promo
> [9ecc969](https://github.com/mozilla/bedrock/commit/9ecc969) - 2015-01-13 - Lam Chi Tak - Bug 504790 - Add new faq for Geolocation
> [d3076c4](https://github.com/mozilla/bedrock/commit/d3076c4) - 2015-01-16 - Alex Gibson - [bug 787269] Redirect signed-script pages to MDN article
> [9e35025](https://github.com/mozilla/bedrock/commit/9e35025) - 2015-01-16 - Alex Gibson - [fix bug 1122462] Download Firefox homepage promo missing small links
> [d8feefa](https://github.com/mozilla/bedrock/commit/d8feefa) - 2015-01-16 - Francesco Lodolo (:flod) - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [ac8be2f](https://github.com/mozilla/bedrock/commit/ac8be2f) - 2015-01-15 - Paul McLanahan - Fix security advisory updater including wrong files.
> [3b032f0](https://github.com/mozilla/bedrock/commit/3b032f0) - 2015-01-15 - Alex Gibson - [fix bug 1121733] Tabs missing from /firefox/tips pages
> [75eab2e](https://github.com/mozilla/bedrock/commit/75eab2e) - 2015-01-15 - Alex Gibson - [fix bug 1121914] Next pager arrow wrong direction on /firefox/desktop/tips
> [a32c254](https://github.com/mozilla/bedrock/commit/a32c254) - 2015-01-14 - Kohei Yoshino - Bug 1121714 - Firefox Desktop Privacy Notice Change (Telemetry Experiments & Domains / Flash)
> [704f515](https://github.com/mozilla/bedrock/commit/704f515) - 2015-01-14 - Jon Petto - Add GA tracking to Fx refresh button. Bug 1027318.
> [862991c](https://github.com/mozilla/bedrock/commit/862991c) - 2015-01-13 - Kohei Yoshino - Fix Bug 1121056 - Wrong date on the ESR release overview image
> [f3bd8c8](https://github.com/mozilla/bedrock/commit/f3bd8c8) - 2015-01-14 - Alex Gibson - [fix bug 1121209] whatsnew page for ESR24 -> ESR31 updates doesn't show Australis tour
> [4a178ca](https://github.com/mozilla/bedrock/commit/4a178ca) - 2015-01-13 - Alex Gibson - [fix bug 787269] Redirect signed-script pages to MDN article
> [19890ac](https://github.com/mozilla/bedrock/commit/19890ac) - 2015-01-13 - Cory Price - [fix bug 1120725] Update link for users with no Hello target
> [64191ab](https://github.com/mozilla/bedrock/commit/64191ab) - 2015-01-13 - Cory Price - [fix bug 1121082] Redirect /hello to /firefox/hello
> [f0d374c](https://github.com/mozilla/bedrock/commit/f0d374c) - 2015-01-13 - Paul McLanahan - Fix bug 1119312: Upgrade Django to 1.6.10.
> [01d2a90](https://github.com/mozilla/bedrock/commit/01d2a90) - 2015-01-13 - Kohei Yoshino - Fix Bug 1121091 - Push legal-docs commits in master to production
> [fdeed74](https://github.com/mozilla/bedrock/commit/fdeed74) - 2015-01-13 - Steven Garrity - Move mozilla-share-cta LESS/CSS into separate file Bug 1121114
> [d2071af](https://github.com/mozilla/bedrock/commit/d2071af) - 2015-01-13 - Francesco Lodolo (:flod) - Bug 1121096 - Hello product page: display video for all Spanish variants
> [face84e](https://github.com/mozilla/bedrock/commit/face84e) - 2015-01-13 - Paul McLanahan - Fix bug 1106845: Move security advisories repo outside of bedrock repo.
> [279d53d](https://github.com/mozilla/bedrock/commit/279d53d) - 2015-01-13 - Paul McLanahan - Fix bug 1120658: Add redirect for seamonkey transition doc.
> [e22a12d](https://github.com/mozilla/bedrock/commit/e22a12d) - 2014-12-11 - Jon Petto - Add refresh button UI to /firefox/new/. Bug 1027318.
> [3ba53d9](https://github.com/mozilla/bedrock/commit/3ba53d9) - 2015-01-13 - Jon Petto - Add defaultUpdateChannel info to UITour docs.
> [9cd35b4](https://github.com/mozilla/bedrock/commit/9cd35b4) - 2015-01-12 - Kohei Yoshino - Fix Bug 1118339 - Update https://www.mozilla.org/en-US/firefox/channel/#aurora for Android ARM links to reflect new FTP directory changes
> [16d1f8f](https://github.com/mozilla/bedrock/commit/16d1f8f) - 2015-01-12 - Josh Mize - Fix bug 1014823 redirect and remove redundant rule
> [a683548](https://github.com/mozilla/bedrock/commit/a683548) - 2015-01-09 - Josh Mize - Add and use bleach_tags filter and fix tests
> [016fc02](https://github.com/mozilla/bedrock/commit/016fc02) - 2015-01-09 - Paul McLanahan - Bug 1119312: Upgrade Django to 1.6.9
> [bbef02c](https://github.com/mozilla/bedrock/commit/bbef02c) - 2015-01-12 - Jon Petto - Update Grameenphone purchase URL for bd. Bug 1120520.
> [9caf848](https://github.com/mozilla/bedrock/commit/9caf848) - 2015-01-12 - Kohei Yoshino - Fix Bug 1118368 - Adjust the style of the Thunderbird start page to accommodate various locales
> [75e0337](https://github.com/mozilla/bedrock/commit/75e0337) - 2014-11-20 - Alex Gibson - [fix bug 1109132] Implement Firefox Hello FTUE
> [8fb68e5](https://github.com/mozilla/bedrock/commit/8fb68e5) - 2015-01-12 - Kohei Yoshino - Fix Bug 1097297 - Link to other systems & languages on the Firefox Developer Edition page
> [73dc10e](https://github.com/mozilla/bedrock/commit/73dc10e) - 2015-01-12 - Alex Gibson - [fix bug 1119022] Hello: zh-TW locale redirects to SUMO article
> [8c8c2d5](https://github.com/mozilla/bedrock/commit/8c8c2d5) - 2015-01-11 - TheoChevalier - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [e9266ad](https://github.com/mozilla/bedrock/commit/e9266ad) - 2015-01-07 - Paul McLanahan - Bug 1118786: Prep deployment and crons for Python 2.7
> [7150d68](https://github.com/mozilla/bedrock/commit/7150d68) - 2014-12-15 - Jon Petto - Add Hello product page. Bug 1101984.
> [bd28123](https://github.com/mozilla/bedrock/commit/bd28123) - 2015-01-09 - Alex Gibson - [fix bug 1118211] Re-enable Firefox Desktop landing animation on OSX
> [769f05d](https://github.com/mozilla/bedrock/commit/769f05d) - 2015-01-09 - Gervase Markham - Address review comment: update redirects.
> [5142217](https://github.com/mozilla/bedrock/commit/5142217) - 2015-01-09 - Gervase Markham - Address review comment: remove now-unnecessary file.
> [c0e1067](https://github.com/mozilla/bedrock/commit/c0e1067) - 2014-12-22 - Kohei Yoshino - Fix Bug 1101220 - Developer Edition follow-ups
> [60e5b46](https://github.com/mozilla/bedrock/commit/60e5b46) - 2014-12-17 - Kohei Yoshino - Fix Bug 1110927 - 301 redirect legacy pages that are 404ing
> [8e93e3d](https://github.com/mozilla/bedrock/commit/8e93e3d) - 2015-01-08 - Jon Petto - Update Fx0 device screenshot. Bug 1116429.
> [4e70573](https://github.com/mozilla/bedrock/commit/4e70573) - 2015-01-06 - Francesco Lodolo (:flod) - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [2001f5b](https://github.com/mozilla/bedrock/commit/2001f5b) - 2015-01-06 - Craig Cook - Fix bug 1114803 - remove EOY fundraiser home promo
> [c5c1d19](https://github.com/mozilla/bedrock/commit/c5c1d19) - 2015-01-07 - Alex Gibson - Update UITour documentation
> [67a53bf](https://github.com/mozilla/bedrock/commit/67a53bf) - 2014-12-29 - Kohei Yoshino - Fix Bug 1115285 - [l10n] Thunderbird start page: make support link localizable
> [7ab0db4](https://github.com/mozilla/bedrock/commit/7ab0db4) - 2015-01-06 - Paul McLanahan - Waffle things default to True when DEV is True.
> [55d8a0e](https://github.com/mozilla/bedrock/commit/55d8a0e) - 2015-01-06 - Paul McLanahan - Fix bug 1116754: Sanitize AJAX returned form errors.
> [fb81024](https://github.com/mozilla/bedrock/commit/fb81024) - 2014-12-17 - Michael Kelly - Bug 1088752: Add Shape of the Web app to serve JSON.
> [9b1a103](https://github.com/mozilla/bedrock/commit/9b1a103) - 2014-12-30 - Francesco Lodolo (:flod) - Bug 1115066 - Add more locales to Thunderbird start page redirect
> [74d6b4d](https://github.com/mozilla/bedrock/commit/74d6b4d) - 2015-01-02 - Craig Cook - Bug 1110966 - remove EOY fundraiser homepage takeover
> [1872bd7](https://github.com/mozilla/bedrock/commit/1872bd7) - 2014-12-19 - Steven Garrity - Bug 1108632 Implement Firefox OS CES landing page
> </pre>

If you've read this far, **THANKS!** We really appreciate the interest.
If you see an issue with this page or site in general click the
edit button below. If you see a problem or have a suggestion for
mozilla.org please [file a bug][]. If you have some reason for wanting
to avoid bugzilla just tweet at me (links around) and
I'm happy to file the bug.

Cheers!

[input]: http://bluesock.org/~willkg/blog/mozilla/input_status_20141218.html
[jakem]: https://github.com/superawesome
[bedrock-doc]: https://wiki.mozilla.org/Websites/Mozilla.org/Static-Media-Improvements
[django-1.6]: https://github.com/mozilla/bedrock/pull/2635
[fxos-tv]: https://www.mozilla.org/firefox/os/devices/tv/
[fx-hello]: https://www.mozilla.org/firefox/hello/
[bedrock-prs]: https://github.com/mozilla/bedrock/pulls
[file a bug]: https://bugzilla.mozilla.org/enter_bug.cgi?product=www.mozilla.org&component=Pages%20%26%20Content
[dino]: http://blog.seanmartell.com/2013/09/17/mozilla-is-my-dinosaur/
