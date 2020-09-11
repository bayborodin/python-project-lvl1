install:
	@poetry install

build:
	@poetry build

run:
	@poetry run brain-games

lint:
	@poetry run flake8 brain_games

publish:
	@poetry publish -r testpypi

.PHONY: install build lint
