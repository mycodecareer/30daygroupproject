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

## build: Build celestia-node binary.
build:
	@echo "--> TODO"
.PHONY: build

## clean: Clean up celestia-node binary.
clean:
	@echo "--> TODO"

## deps: install dependencies.
deps:
	@echo "--> TODO"
.PHONY: deps

## lint: Linting *.go files using golangci-lint. Look for .golangci.yml for the list of linters.
lint: 
	@echo "--> Running Linters"
	@markdownlint --config .markdownlint.yaml '**/*.md'
	@flake8 --max-line-length 88 --ignore E203,E501,W503,W605,E722
	@black --check .
	@yamllint --no-warnings .
.PHONY: lint

fmt:
	@echo "--> Auto Formatting"
	@black .
	@markdownlint --config .markdownlint.yaml '**/*.md' -f
.PHONY: fmt

## test-all: Running both unit and swamp tests
test:
	@echo "--> TODO"
.PHONY: test
