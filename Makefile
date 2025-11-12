.PHONY: install test

install:
	pip install -r requirements.txt

test: install
	@echo "🔍 Running tests..."
	pytest -v tests/
