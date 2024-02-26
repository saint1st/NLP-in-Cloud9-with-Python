install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

	python -m textblob.download_corpora

test:
	
	python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py
	

lint:
	pylint --disable=R,C,E1120 *.py nlplogic/*.py
	
format:
	black *.py

all: install lint test