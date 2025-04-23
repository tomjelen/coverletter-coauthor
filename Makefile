.PHONY: clean test serve-dev

venv: requirements.txt
	python3 -m venv venv --clear --prompt clg
	venv/bin/pip install -r requirements.txt

test: venv
	venv/bin/pytest

serve-dev: venv
	venv/bin/fastapi dev rest_api/api.py

clean:
	rm -rf venv
