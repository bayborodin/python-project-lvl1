install:
	@poetry install

build:
	@poetry build

run:
	@poetry run brain-games

lint:
	@poetry run flake8 brain_games

.PHONY: install build lint
