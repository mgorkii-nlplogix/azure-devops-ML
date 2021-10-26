install:
	pip install --upgrade pip &&\
    	pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py


lint:
	pylint --disable=R,C hello.py

venv:
	python3 -m venv .venv &&\
		
source:
	. ./.venv/bin/activate

all: install lint test