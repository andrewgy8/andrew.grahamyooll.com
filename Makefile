bakesite:
	./bakesite.py

serve: bakesite
	echo Running Python http.server ...; \
	cd _site && python3 -m http.server 8003;

loc:
	grep -vE '^[[:space:]]*#|^[[:space:]]*$$|^[[:space:]]*"""' bakesite.py | wc -l
