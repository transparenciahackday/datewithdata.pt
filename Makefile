build:
	gulp build

install:
	npm install

serve:
	gulp watch

deploy:
	gulp build
	rsync -ar --delete --progress dev/ -e ssh dh:~/www/datewithdata.pt/
dry-deploy:
	rsync -arn --delete --progress dev/ -e ssh dh:~/www/datewithdata.pt/
