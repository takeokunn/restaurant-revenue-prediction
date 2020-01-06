.PHONY: notebook
notebook:
	docker-compose up notebook

.PHONY: script
script:
	docker-compose run --rm script

.PHONY: convert
convert:
	docker-compose run --rm script jupyter nbconvert --to script jupyter/notebook.ipynb --output-dir=src/

.PHONY: download
download:
	kaggle competitions download -p assets -c restaurant-revenue-prediction
	unzip -d assets/ assets/restaurant-revenue-prediction.zip
	unzip -d assets/ assets/test.csv.zip
	unzip -d assets/ assets/train.csv.zip

.PHONY: submit
submit:
	kaggle competitions submit -c restaurant-revenue-prediction -f output/submission.csv -m "Submit!"
