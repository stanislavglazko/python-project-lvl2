install:
	@poetry install

lint:
	@poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

run_test:
	poetry run coverage run -m pytest gendiff tests


.PHONY: install test lint selfcheck check build
