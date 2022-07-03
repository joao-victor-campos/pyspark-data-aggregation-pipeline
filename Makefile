# globals
VERSION := $(shell grep __version__ spark_pipeline/__metadata__.py | head -1 | cut -d \" -f2 | cut -d \' -f2)

.PHONY: requirements-dev
## install development requirements
requirements-dev:
	@python -m pip install -U -r requirements.dev.txt

.PHONY: requirements-minimum
## install prod requirements
requirements-minimum:
	@python -m pip install -U -r requirements.txt

.PHONY: requirements
## install requirements
requirements: requirements-dev requirements-minimum

.PHONY: tests-coverage
## run unit and integration tests with coverage report
tests-coverage:
	@echo ""
	@echo "Tests"
	@echo "=========="
	@echo ""
	@pytest --cov-report term --cov-report html:tests-cov --cov=spark_pipeline --cov-fail-under=40 --ignore=tests/e2e ./tests/

.PHONY: unit-tests
## run unit tests
unit-tests:
	@echo ""
	@echo "Unit Tests"
	@echo "=========="
	@echo ""
	@python -m pytest tests/unit

.PHONY: integration-tests
## run integration tests
integration-tests:
	@echo ""
	@echo "Integration Tests"
	@echo "================="
	@echo ""
	@python -m pytest tests/integration

# .PHONY: e2e-tests
# ## run e2e tests with infrastructure on docker compose
# e2e-tests:
# 	@echo ""
# 	@echo "E2E Tests"
# 	@echo "================="
# 	@echo ""
# 	@docker compose -f tests/e2e/docker-compose.yaml up --build e2e

# .PHONY: app
# ## create db infra with docker compose
# app:
# 	@docker compose -f tests/e2e/docker-compose.yaml run app bash

# .PHONY: teardown
# ## teardown all infra on docker compose
# teardown:
# 	@docker compose -f tests/e2e/docker-compose.yaml down

.PHONY: style-check
## run code style checks with black
style-check:
	@echo ""
	@echo "Code Style"
	@echo "=========="
	@echo ""
	@python -m black --check --exclude="build/|buck-out/|dist/|_build/|pip/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" . && echo "\n\nSuccess" || (echo "\n\nFailure\n\nRun \"make black\" to apply style formatting to your code"; exit 1)

.PHONY: quality-check
## run code quality checks with flake8
quality-check:
	@echo ""
	@echo "Flake 8"
	@echo "======="
	@echo ""
	@python -m flake8 && echo "Success"
	@echo ""

.PHONY: type-check
## run code type checks with mypy
type-check:
	@echo ""
	@echo "Mypy"
	@echo "======="
	@echo ""
	@python -m mypy --install-types --non-interactive spark_pipeline && echo "Success"
	@echo ""

.PHONY: checks
## run all code checks
checks: style-check quality-check type-check

.PHONY: apply-style
## fix stylistic errors with black and isort
apply-style:
	@python -m black --exclude="build/|buck-out/|dist/|_build/|pip/|\\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" .
	@python -m isort spark_pipeline/ tests/

.PHONY: package
## build spark_pipeline package wheel
package:
	@python -m setup sdist bdist_wheel

.PHONY: version
## show version
version:
	@echo "$(VERSION)"

.PHONY: build-docker
## build spark_pipeline image
build-docker:
	@docker build -t spark_pipeline:$(VERSION) \
	-t spark_pipeline:latest .

.PHONY: clean
## clean unused artifacts
clean:
	@find ./ -type d -name 'dist' -exec rm -rf {} +;
	@find ./ -type d -name 'build' -exec rm -rf {} +;
	@find ./ -type d -name 'spark_pipeline.egg-info' -exec rm -rf {} +;
	@find ./ -type d -name 'htmlcov' -exec rm -rf {} +;
	@find ./ -type d -name '.pytest_cache' -exec rm -rf {} +;
	@find ./ -type d -name 'spark-warehouse' -exec rm -rf {} +;
	@find ./ -type d -name 'metastore_db' -exec rm -rf {} +;
	@find ./ -type d -name '.ipynb_checkpoints' -exec rm -rf {} +;
	@find ./ -type f -name 'coverage-badge.svg' -exec rm -f {} \;
	@find ./ -type f -name 'coverage.xml' -exec rm -f {} \;
	@find ./ -type f -name '.coverage*' -exec rm -f {} \;
	@find ./ -type f -name '*derby.log' -exec rm -f {} \;
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*.pyo' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
## @find ./ -name '*.mypy_cache' -exec rm -rf {} \;

.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')