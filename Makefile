.PHONY: test

deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt

lint:
		flake8 test
		# instalacja flake8: python -m pip install flake8

test:
		PYTHONPATH=. py.test
		PYTHONPATH=. py.test  --verbose -s

run:
		python testy.py
