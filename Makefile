install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest

lint:
	ruff check .

format:
	black .

coverage:
	pytest --cov=src

notebook:
	jupyter lab
