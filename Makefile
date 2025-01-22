makesite:
	./makesite.py

serve: makesite
	echo Running Python http.server ...; \
	cd _site && python3 -m http.server 8003;

publish: makesite
	cp CNAME _site
	cp .nojekyll _site
	git add .
	git commit -m 'Publish site'
	git subtree push --prefix _site origin gh-pages

loc:
	grep -vE '^[[:space:]]*#|^[[:space:]]*$$|^[[:space:]]*"""' makesite.py | wc -l

FORCE:
