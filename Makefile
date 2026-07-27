install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pip install -e .


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

run:
	python src/project_north/cli/main.py "Benjamin Lebrun" 12 11 1997