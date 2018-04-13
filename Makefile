.PHONY: test

deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt
		python -m pip install flake8

lint:
		flake8 test

test:
		PYTHONPATH=. py.test testy.py
		#PYTHONPATH=. py.test  --verbose -s

run:
		python testy.py
