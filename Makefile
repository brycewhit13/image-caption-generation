setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	python3 setup.py develop

format:
	black *.py
	black caption/*.py

lint: 
	pylint --disable=R,C caption/generate_caption.py

test:
	python3 -m pytest -vv --cov=caption/generate_caption caption/test_generate_caption.py

all: setup format lint test