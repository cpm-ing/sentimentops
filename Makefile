.PHONY: setup lint test

setup:
python -m pip install -r requirements.txt

lint:
ruff check src/ tests/

test:
pytest tests/ -v
