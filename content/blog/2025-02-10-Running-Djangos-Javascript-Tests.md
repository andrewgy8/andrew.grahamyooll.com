---
title: Running Django's Javascript Tests
tags:
  - Engineering
---

Django has lots of tests, and wide range of types:
- unit tests with Unittest
- UI/Selenium tests
- Screenshots
- Javascript QUnit tests

I recently dug into an issue with Django, and was confronted with which type of test I to create. Exploring the codebase, I ended up running all 4 of the types of tests to explore my options. 

All of them ran successfully following the Django Docs, except for the [Javascript tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/javascript/#running-tests). 

When I changed a value or assertion in the Javascript test, the change was not reflected in the test runner. As a result, I was properly flustered for an hour or so of debugging.

The Javascript testing docs need a bit of work, but in the meantime this guide should suffice to solve the issue:

1. Run `npm install`
2. Run `python -m http.server`
3. Open  [http://localhost:8000/js_tests/tests.html](http://localhost:8000/js_tests/tests.html) in your INCOGNITO browser.
4. Make a change, and the tests will run again on refresh. 

I haven't dove into too deeply, but I suspect the local cache plays a role in the unexpected behaviour. 

