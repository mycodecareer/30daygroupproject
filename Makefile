SHELL=/usr/bin/env bash
PROJECTNAME=$(shell basename "$(PWD)")

## help: Get more info on make commands.
help: Makefile
	@echo " Choose a command run in "$(PROJECTNAME)":"
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
.PHONY: help

## install: Install git-hooks from .githooks directory.
install-hooks:
	@echo "--> Installing git hooks"
	@git config core.hooksPath .githooks
.PHONY: init-hooks

build:
	@echo "--> TODO"
.PHONY: build

clean:
	@echo "--> TODO"

deps:
	@echo "--> TODO"
.PHONY: deps

## lint: Run all linters for the project.
lint: 
	@echo "--> Running Linters"
	@markdownlint --ignore 'frontend/node_modules/**' --config .markdownlint.yaml '**/*.md'
	@flake8 --max-line-length 88 --ignore E203,E501,W503,W605,E722
	@black --check .
	@yamllint --no-warnings .
	@cd frontend && yarn prettier --check . && cd ..
.PHONY: lint

## fmt: Auto format the code based on the linters
fmt:
	@echo "--> Auto Formatting"
	@black .
	@markdownlint --ignore 'frontend/node_modules/**' --config .markdownlint.yaml '**/*.md' -f
	@yarn prettier --write .
.PHONY: fmt

## test: run all tests in the project
test:
	@echo "--> TODO"
.PHONY: test

## backend-test: run all the backend tests
backend-test:
	@echo "--> Running Backend Tests"
	@pytest -v
.PHONY: backend-test
