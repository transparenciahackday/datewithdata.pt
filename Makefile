build:
	mkdir -p _build
	cp -ar assets/index.html _build
	cp -ar assets/favicons _build
	cp -ar assets/fonts _build
	cp -ar assets/foundation-icons _build
	cp -ar assets/images _build
	cp -ar assets/pages _build
	cp -ar --no-target-directory assets/scripts _build/js
	mkdir -p _build/css
	./lib/sass --style compressed --no-source-map --quiet assets/styles/app.scss _build/css/app.min.css

serve:
	cd _build && python -m SimpleHTTPServer

deploy: build
	rsync -ar --delete --update --progress _build/ -e ssh dh:/home/rlaf/www/datewithdata.pt/
dry-deploy: build
	rsync -arn --delete --update --progress _build/ -e ssh dh:/home/rlaf/www/datewithdata.pt/
