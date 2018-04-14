.PHONY: test

deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt
		
lint:
		flake8 test

test:
		PYTHONPATH=. py.test testy/testy.py
		
run:
		python testy.py
