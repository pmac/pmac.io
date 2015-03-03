title: The State of Mozilla.org - February 2015
tags: mozilla, bedrock, somo
date: 2015-03-03 13:00
summary: Monthly update on what's been happening with www.mozilla.org

Hello all! It's already been a month since last we spoke and much has happened! Let's get to it.

Note: It appears that monthly will be a better schedule for these than every 2 weeks, at least for me. I'll try to keep to that. Please call me out if I fail.

## Theme for February: ZOMG BUSY!

February is always a busy month for we developers in the Engagement team, at least since Mozilla broke into the mobile world with Fennec and Firefox OS. This is because the first of March is [Mobile World Congress](https://en.wikipedia.org/wiki/Mobile_World_Congress) (MWC) time, and it's always a scramble to get things done in time. I concentrate mostly on the server side of the Web, but my colleagues in [Web Prod][] who deal in HTML, CSS, and JS were more than a little busy. They launched a [new page for MWC](https://www.mozilla.org/mwc/), a new [Firefox OS main page](https://www.mozilla.org/firefox/os/), a new consolidated nav for all of that, and updates to various other FxOS related pages to support announcements. It was a herculean effort, the results are amazing, and I'm more than a little proud to work with them all. Special thanks to our new staff-member teammate [Schalk Neethling][] for going way above and beyond to get it all done.

Also, long time friend of mozilla.org [Craig Cook](https://github.com/craigcook) knocked out a refresh of the [Mozilla Leadership page](https://www.mozilla.org/about/leadership/). Nice work Craig!

Not only all of that, but February saw a major overhaul of how bedrock handles static assets (CSS, LESS, JS, Fonts, Images, etc.). It's all part of [the plan](https://wiki.mozilla.org/Websites/Mozilla.org/Static-Media-Improvements). There's more to come.

1. We have finally moved into the modern world (speaking in Django terms) and are using the [staticfiles][] system. We are now free to do things like handle user-uploaded media, use new and cool tools, and not feel bad about ourselves.
2. We've switched from jingo-minify to [django-pipeline][]. Pipeline hooks into Django's static media system and is therefore easier to integrate with other parts of the Django ecosystem as well as more customizable. It is also a much more active project and supports a lot of fun new things (e.g. Babel-JS for sweet sweet ES6 goodness in our ES5 world).
3. Good Olde Apache™ used to be how we served our static assets, but we're now doing that from bedrock itself using [Whitenoise][]. Since we have a CDN the traffic for these files on the server is quite low so getting cache headers, CORS, and gzipping right is the most important thing. Whitenoise handles all of this efficiently and automatically. I highly recommend it.

With these new toys came the ability to generate what are called "[Immutable Files](https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#cachedstaticfilesstorage)". This means that the system will now copy all static files to new filenames that include the md5 hash of the file contents. This means that the file name (e.g. site.4d72c30b1a11.js) will always necessarily refer to the same contents. The advantage of this is that we can set the cache headers to basically never expire. Any time the file content changes, the generated file name will be different and cached separately.

We're also generating gzipped versions of all files at deploy time. Whitenoise will see that these files exist (e.g. site.4d72c30b1a11.js.gz) and serve up the compressed version when the browser says it can handle it (and nearly all can these days). This is good because this is no longer happening at request time in Apache, thus reducing load, and we can use better and slower compression since it's happening outside of the request process.

Much more happened, but I'm loath to make this much longer. Skim the git log below for the full list.

[staticfiles]: https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/
[django-pipeline]: http://django-pipeline.readthedocs.org/
[Whitenoise]: http://whitenoise.evans.io/

## Contributors

Even more new contributors! ***HOORAY!***

* [blisman](https://github.com/lismanb) started contributing to bedrock this month and has already fixed 3 bugs!
* The aforementioned [Schalk Neethling][] is new to the team, but not Mozilla nor FLOSS contribution, nor even bedrock as he's maintained the [Plugin Check](https://www.mozilla.org/plugincheck/) page for quite some time. He did a wonderful job on the new Firefox OS page.
* [Kohei Yoshino](https://github.com/kyoshino) continues dominating all the things and even got yet another [Friend of The Tree](https://wiki.mozilla.org/WeeklyUpdates/2015-03-02#Friends_of_Mozilla) (Friends of Mozilla) mention.
* [Stephanie Hobson](https://github.com/stephaniehobson) (on loan from MDN) stepped up to help us with some changes in preparation for the new Firefox for iOS (coming soon to an iDevice near you).

Thank you all for your contributions to bedrock and the Open Web **\o/**

[Web Prod]: https://wiki.mozilla.org/Webdev/Web_Production
[Schalk Neethling]: https://github.com/schalkneethling

## [Git Log for February](https://github.com/mozilla/bedrock/compare/8547262...c0dfdee)

<div class="git-log" markdown="1">
* 8547262 (Pascal Chevrel) Bug 1128957 - Fix block parsing errors in jinja templates
* bb8aa7a (Kohei Yoshino) Fix Bug 1129130 - Hyperlinking bios to Steering Committee page
* f67af74 (Kohei Yoshino) Fix Bug 1129214 - Please add Rust and Cargo to our trademark list
* 80c4b28 (Kohei Yoshino) Fix Bug 1128885 - Plugincheck-site considers 31.4.0ESR out of date
* 7664dc5 (Alex Gibson) Update UITour documentation
* d0c20a4 (Tim) updated sumo link to be locale-neutral
* f588ff8 (Craig Cook) Fix bug 1124826 - Net Neutrality home promo
* 5475a14 (Paul McLanahan) Add new contributors to humans.txt
* 68a927c (Kohei Yoshino) Fix Bug 1124724 - Tiles product page update copy mozilla.org/en-US/firefox/tiles/
* 64c4f17 (Paul McLanahan) Fix bug 1130285: Treat hsb/dsb locales as de for number formatting.
* ea43c4e (Kohei Yoshino) Fix Bug 1129911 - Text error in https://www.mozilla.org/en-US/about/governance/policies/commit/
* e5496d6 (Francesco Lodolo (:flod)) Bug 1115066 - Add 'si' to Thunderbird start page redirect
* 776cff3 (Alex Gibson) Add test suite for browser-tour.js
* 73295a6 (Tin Aung Lin) Updated with new Facebook Page Link
* 43909f2 (Kohei Yoshino) Fix Bug 1131142 - Update Firefox Refresh SUMO article link on /firefox/new/
* 9a4de71 (Alex Gibson) [fix bug 1131680] Stop redirecting Firefox Geolocation page to Mozilla Taiwan website
* a502fe1 (Kohei Yoshino) Fix Bug 1130160 - Extra '#' in section headers for roll up pages
* 6aaee9f (Paul McLanahan) Fix bug 1131738: Mark advisory reporter as safe.
* 90aabcb (Paul McLanahan) Bug 906176: Move to using Django staticfiles for media.
* 66541a9 (Paul McLanahan) Bug 906176: Enable caching static storage and remove cachebusts.
* 63da90f (Paul McLanahan) Update references to "media()" in docs.
* 286c35c (Paul McLanahan) Bug 906176: Move to django-pipeline from jingo-minify.
* 6fdbc53 (Paul McLanahan) Add futures, a dependency of pipeline.
* 3a200c0 (Paul McLanahan) Add node dependencies less and yuglify.
* a3b0895 (Paul McLanahan) Reorder deployment to keep the git repo clean.
* 56b89a1 (Paul McLanahan) Serve static files with Whitenoise.
* c96ba80 (Paul McLanahan) No longer test Python 2.6 in Travis.
* ae040d4 (Paul McLanahan) Fix unicode issue with image helpers.
* f9849c7 (Kohei Yoshino) Fix Bug 1131111 - PN Changes (Snippets/SMS Campaign, default Search provider, and SSL Error reporting)
* a61fd11 (Paul McLanahan) Disable locale sync from crons temporarily.
* c5cbfd7 (Paul McLanahan) Enable locale update cron jobs; they are now fixed.
* f8ced59 (Paul McLanahan) Fix missing image referenced in thunderbird base template.
* 1592de3 (Paul McLanahan) Fix bug 1132317: Fix gigabit pages errors.
* b8e2afd (Paul McLanahan) Remove remaining date-based cache busting query params.
* 6eb5107 (Logan Rosen) fix Bug 1132323: change Tabzilla heading ID
* cdadc8a (Logan Rosen) fix Bug 1108278: congstar link is incorrect
* 453ae78 (Paul McLanahan) Encourage use of humans.txt
* d3c553d (Alex Gibson) [fix bug 1132289] Plugin check minify JS error
* 375b3b3 (schalkneethling) Syncing content with Google doc, part of the l10n hand-over
* b4c217e (Jon Petto) Bug 1128726. Add 2 new firstrun tests, each with 2 variants.
* 8ccad60 (Alex Gibson) [fix bug 1132313] Venezuela community page references missing images
* f74b2a7 (Paul McLanahan) Fix bug 1132454: Update platform_img helper for new static files.
* fd4215b (Alex Gibson) [bug 1132454] Add missing high-res ios platform image to firefox/new
* 5184b79 (Alex Gibson) Update Mozilla.ImageHelper JS tests
* 03d7b14 (Kohei Yoshino) Fix Bug 1132835 - 404 linking to /contribute/local from /about/governance/organizations
* ec262fe (Paul McLanahan) Fix bug 1132961: Add cache to twitter feeds.
* a420c03 (Kohei Yoshino) Fix Bug 1132956 - Legal-docs pages for hu and hr throwing errors.
* 61dea65 (Kohei Yoshino) Fix pep8 errors: W503 line break before binary operator
* ad3f3c8 (Francesco Lodolo (:flod)) Bug 1124894 - Add Swahili (sw) to PROD_LOCALES
* 6193a4f (Jon Petto) Bug 1130565. Add more localized videos to Hello page.
* e41a55f (blisman) fix bug  1132942, removed url for missing html template  (/bedrock/mozorg/about/governance/policies/commit/faq.html)
* 89ad7c1 (blisman) Bug 1134492 - move assets from assets.mozilla.org to assets.mozillalabs.com
* 43ac8cd (Alex Gibson) [fix bug 1053214] Missing Mozilla Estonia from Contact Pages
* a3cb7e5 (Stephanie Hobson) Fix Bug 1134058: Show .form-details when form has focus
* 0307a5b (Paul McLanahan) Only build master in Travis.
* 4990787 (Cory Price) [fix bug 1130198] Update Hello FTU for GA36 * Send Custom Variable to GA containing the referral * Add referral to localStorage on copy/email link * Retreve referral from localStorage on tour connect and send to GA * Hide info panels when Contacts tab is clicked (it's okay that they don't see it if they switch back to Rooms) * Update docs * Add Test
* 4f7a542 (Paul McLanahan) Add author link tag to base templates for humans.txt
* c452ac0 (Kohei Yoshino) Fix Bug 1134936 - Firefox download pages: filter localized builds as you type
* d681e78 (Josh Mize) Add backend for fxos feed links: bug 1128587
* 4a81001 (Josh Mize) Restore dev update crons: fix bug 1133942
* f0ab7b5 (Steven Garrity) Bug 1120689 MWC Preview page for 2015
* e6d9ada (blisman) fix bug 1129961: reps ical feed update fail silently
* 54b27ed (Paul McLanahan) Remove accidentially committed print statement.
* d406fb0 (Steven Garrity) Bug 1120689 Update MWC map reference
* 2592f4f (Alex Gibson) [fix bug 1135496] Missing Firefox OS wordmark on devices page
* 259f1d2 (Alex Gibson) [fix bug 1099471 1084200] Implement Firefox Hello tours GA 36
* eb6471a (Jon Petto) Add firstrun and whatsnew pages. Bug 1099471.
* e797b42 (Alex Gibson) Update Hello fx36 tour logic and add tests
* 93a6f2e (Alex Gibson) Add Fx36 Hello tour GA tracking events
* 2500616 (Jon Petto) Hello tour updates:
* 7b7329e (Steven Garrity) Bug 1120689 Last minute MWC preview text tweaks
* 8859e9c (Alex Gibson) Fx36 Hello tour template updates
* 5dde0d1 (Kohei Yoshino) Improve the Share widget, part of Bug 1131309
* d6d4ab6 (Kohei Yoshino) Fix Bug 1131309 - Add share buttons to 'Check your plugins' page
* 0a3dea6d (Steven Garrity) Bug 1120689 Update map for MWC 2015 Removed the link to the PDF and used a single PNG for mobile/desktop
* b0eced3 (Paul McLanahan) Bug 1116511: Add script to sync data from Tableau.
* acca704 (Paul McLanahan) Bug 1116511: Add view for serving JSON contributor data.
* b807b1a (Paul McLanahan) Bug 1116511: Add cron jobs for stage and prod tableau data.
* e27fa38 (Kohei Yoshino) Fix Bug 1128579 - Finish moving certs/included and certs/pending web pages to wiki pages
* 34f032d (Paul McLanahan) Fix a potential error in the TwitterCacheManager.
* 5fa4fb3 (Steven Garrity) Bug 1120667 Remove "over" from MWC preview page
* d627564 (Francesco Lodolo (:flod)) Bug 1111597 - Set up Santali (sat) for production
* 20afbf3 (Craig Cook) Update home page promos
* f727d1a (Cory Price) [fix bug 1130194] Add FTU tracking to Hello product page
* 3ec1f54 (Kohei Yoshino) Fix Bug 1136224 - firefox hello privacy policy link to tokbox privacy policy broken
* 59b7b09 (Paul McLanahan) Fix bug 1136307: Catch all errors and report exceptions for MFSA import.
* c4d1534 (schalkneethling) Fix Bug 1132298 Moves mustache script above the share script
* 41c8b12 (Craig Cook) Bug 1132231 - fix copy for Webmaker and Hello promos
* 0963b2a (Kohei Yoshino) Standardize the header share button
* 4fdd9f0 (Kohei Yoshino) Fix Bug 1131304 - Add share buttons to 'Download Firefox in your language' page
* f53b05f (Kohei Yoshino) Fix Bug 1131299 - Add share buttons to Firefox Developer Edition page
* 2c8a27f (Steven Garrity) Bug 1120689 Update title on MWC preview for 2015
* 9ab3132 (Paul McLanahan) Fix bug 1136559: Add dev deploy cron scripts to repo.
* 4b36ba5 (Stephanie Hobson) Fix Bug 1126578: iOS CTA updates and newsletter
* c8b7a5f (Stephanie Hobson) Bug 1126578: iOS CTA updates and newsletter
* d53c578 (Kohei Yoshino) Fix Bug 1126837 - Make Fx38 Win64 build of Dev Edition Available on moz.org
* acf34be (Kohei Yoshino) Fix Bug 1137213 - Sky theme is not applied to Firefox channel page if Developer Edition is selected first
* 934fe4c (Jon Petto) Bug 1135092. Fx family nav V1.
* 5e8d55d (Paul McLanahan) Get current hash from local file and run dev autodeploy every 20min.
* 6984385 (Paul McLanahan) No output for dev autoupdate unless deploying.
* f6a6fad (Kohei Yoshino) Fix Bug 1137061 - Firefox Release Notes list shows unsorted sub-versions
* f8a5358 (Kohei Yoshino) Fix Bug 1137604 - /security/advisories: abbreviation mismatch: MSFA vs. MFSA
* d8572fe (Jon Petto) Bug 1135092. Add small IE fixes to fx family nav v1.
* 8847d9f (Jon Petto) Bug 1137260. Add GA to fx family nav.
* 4f16a2b (Josh Mize) Update firefox os feeds on dev deploy
* 05bc712 (Craig Cook) Fix bug 1134522 - New leadership page
* b966d62 (Paul McLanahan) Remove locale update from deployment.
* 9ed05bc (Steven Garrity) Bug 1120686 Update Fx Partners page for MWC 2015
* d0bf649 (Jon Petto) Bug 1137904. Add headlines to MWC page.
* 97685f5 (Steven Garrity) Bug 1137347 Add temporary links to static logos
* b03989e (Steven Garrity) Add All press link
* b0440e9 (schalkneethling) Fix Bug 1120700, implement new design for firefox/os
* 5ac9fe3 (Steven Garrity) Bug 1120686 Fix overlaping menus Mobile partners nav was overlapping family nav submneu due to excessive z-index
* 1de1bfc (Steven Garrity) Bug 1137347 Use https for static images
* 431aea6 (Paul McLanahan) Update static files, product-details, and external files in SRC dir.
* ebfd67a (Craig Cook) Bug 1120700 - Misc tweaks and fixes for new FxOS page
* b6225ee (Paul McLanahan) Update revision.txt before collectstatic.
* e8c9f28 (Craig Cook) Bug 1124734 - remove Net Neutrality promo after Feb 26
* c0066c1 (Craig Cook) Fix bug 1138169 - MWC partner logo updates
* 90bec7a (Francesco Lodolo (:flod)) Bug 1120700 - Fx OS consumer page: restore page title on old template
* c0dfdee (Steven Garrity) Bug 1137347 Replace temporary MWC logos
</div>
