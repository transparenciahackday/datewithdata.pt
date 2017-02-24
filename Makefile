build:
	gulp build

install:
	npm install

serve:
	gulp watch

deploy:
	rsync -ar --delete --progress _build/ -e ssh dh:/home/rlaf/www/datewithdata.pt/
dry-deploy:
	rsync -arn --delete --progress _build/ -e ssh dh:/home/rlaf/www/datewithdata.pt/
