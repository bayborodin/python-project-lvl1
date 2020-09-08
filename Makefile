install:
	@poetry install

build:
	@poetry build

run:
	@poetry run brain-games

.PHONY: install build
