.PHONY: help install dev-install validate format lint clean pre-commit

help:
	@echo "Playing Cards - Development Commands"
	@echo "===================================="
	@echo "make install       - Install dependencies"
	@echo "make dev-install   - Install development dependencies"
	@echo "make validate      - Run HTML/CSS validation"
	@echo "make format        - Format Python code"
	@echo "make lint          - Lint Python code"
	@echo "make pre-commit    - Install pre-commit hooks"
	@echo "make clean         - Clean build artifacts"

install:
	pip install -e .

dev-install:
	pip install -r requirements-dev.txt
	pip install -e .

validate:
	python validate.py

format:
	black validators/ validate.py
	isort validators/ validate.py

lint:
	black --check validators/ validate.py
	isort --check validators/ validate.py

pre-commit:
	pre-commit install

clean:
	rm -rf __pycache__
	rm -rf validators/__pycache__
	rm -rf *.pyc
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
