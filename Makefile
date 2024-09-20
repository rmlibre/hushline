.DEFAULT_GOAL := help

.PHONY: help
help: ## Print the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		column -s ':' -t

.PHONY: install
install:
	poetry install
	npm install

.PHONY: run
run: ## Run the app
	. ./dev_env.sh && \
	poetry run flask run --debug -h localhost -p 8080

.PHONY: migrate-dev
migrate-dev: ## Run dev env migrations
	poetry run ./scripts/dev_migrations.py

.PHONY: migrate-prod
migrate-prod: ## Run prod env (alembic) migrations
	poetry run flask db upgrade

.PHONY: lint
lint: ## Lint the code
	poetry run ruff format --check && \
	poetry run ruff check && \
	poetry run mypy .
	npx prettier --check .

.PHONY: fix
fix: ## Format the code
	poetry run ruff format && \
	poetry run ruff check --fix
	npx prettier --write .

.PHONY: revision
revision: migrate-prod ## Create a new migration
ifndef message
	$(error 'message' must be set when invoking the revision target, eg `make revision message="short message"`)
endif
	poetry run flask db revision -m "$(message)" --autogenerate

.PHONY: test
test: ## Run the test suite
	docker compose run --rm app \
		poetry run pytest --cov hushline --cov-report term --cov-report html -vv tests/$(test)
