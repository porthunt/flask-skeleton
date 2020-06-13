SHELL := /bin/bash

init:
	@pip install -r requirements.txt

lint:
	flake8 app/ run.py settings.py
	black --line-length 79 --check app/ run.py settings.py

unit:
	pytest --disable-pytest-warnings ./tests/unit/

test: lint unit

