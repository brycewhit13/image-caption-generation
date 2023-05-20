install: 
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	./format.sh

lint: 
	pylint --disable=R,C caption/generate_caption.py

test:
	python -m pytest -vv --cov=caption/generate_caption caption/test_generate_caption.py