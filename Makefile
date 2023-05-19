install: 
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black *.py

lint: 
	pylint --disable=R,C generate_caption.py

test:
	python -m pytest -vv --cov=generate_caption test_generate_caption.py