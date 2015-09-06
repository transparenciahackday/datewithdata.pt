build:
	gulp

install:
	npm install

serve:
	gulp watch

deploy:
	rsync -aru --delete --progress dev/ -e ssh dh:~/www/datewithdata.pt/
dry-deploy:
	rsync -arun --delete --progress dev/ -e ssh dh:~/www/datewithdata.pt/
