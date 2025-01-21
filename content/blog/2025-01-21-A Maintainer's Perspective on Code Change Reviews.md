<!-- title:Don't be The Asshat: A Maintainer's Perspective on Code Change Reviews -->

What most people underestimate about open source is that creating a PR is only the first hurdle to jump through. For better or worse, contributing changes to any open-source software is difficult and generally met with friction and delay.

Here, I will present different ways a PR review can turn out from a maintainer's (MY) perspective.

Receiving approval from the voices that have the power to merge a change is a completely different experience from writing the initial code.

There are three general ways a review can go:

1. **Easy-Peasy:**  
	It can be a great collaboration with basic format change requests, or, if you’re really lucky, no issues because the formatting infra (linting, testing, etc.) is all there and the implementation and issues have already been pounded out before the PR is put up. **From a maintainer's perspective, those are the best reviews to look over, and you always want to strive for this as a contributor.**
	
2. **Back and Forth:**  
	A drawn-out review but resulting in changes to code throughout the PR process. From a maintainer's perspective, these are fine as PRs are, by design, a collaborative experience. Personally, I'm more than happy to help out as much as possible to get your changes into the main branch. I want to see you create value in the project and become more involved.
	
3. **The Asshat:**  
	Lastly, there’s the cringey scenario that I see all too often where a wanna-be contributor refuses to collaborate. Generally, the contributor says "No" to all suggestions. Even worse, they say, "No, let's try it out" or "It'll be fine." Like, no, I'm not going to merge your stuff that I don't agree with or, worse, put some sketchy code into the main dist that may or may not work. I want 99.99% confidence that this is going to work.

As a maintainer, I understand that reviews may seem like friction-filled formalities. And to be clear, I don't mind pushback on some suggestions. But when multiple maintainers are pushing for the same suggestion, think about it. Harness your humility.

Code reviews are indeed a brake on changes for all maintainers to understand what the changes are doing and why they are being accepted. As a maintainer, if something breaks with the change, we are most likely going to be the ones to fix the issue.

As stated above, open source is hard. So, no, I won't be YOLO'ing your changes to the main build of a large library.

Any other maintainers feel the same way? Let me know via email andrewgy8[at]gmail.com