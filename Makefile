install:
	@poetry install

build:
	@poetry build

lint:
	@poetry run flake8 brain_games

publish:
	@poetry publish -r testpypi

.PHONY: install build lint
