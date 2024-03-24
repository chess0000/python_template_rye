# install
.PHONY: install
install:
	rye pin 3.12
	rye sync
	rye run pre-commit install
	cp .env.example .env
	mkdir logs

# main.pyを実行する
.PHONY: run_main
run_main:
	python3 src/main.py

# pre-commitを明示的に実行する
.PHONY: pre-commit
pre-commit:
	rye run pre-commit run --all-files

.PHONY: format
format:
	rye run format

.PHONY: lint
lint:
	rye run lint

.PHONY: test
test:
	rye run test
