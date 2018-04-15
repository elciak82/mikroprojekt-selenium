SERVICE_NAME=testy-zrabatowani
MY_DOCKER_NAME=$(SERVICE_NAME)

.PHONY: test
.DEFAULT_GOAL :=test

deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt

lint:
		flake8 test

test:
		PYTHONPATH=. py.test testy/testy.py

run:
		python testy/testy.py

docker_build:
			docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
			docker run \
							--name $(MY_DOCKER_NAME)-dev \
							-p 5000:5000 \
							-d $(MY_DOCKER_NAME)

docker_stop:
		docker_stop $(MY_DOCKER_NAME)-dev

USERNAME=zrabatowani
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

docker_push: docker_build
				@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
				docker tag $(MY_DOCKER_NAME) $(TAG); \
				docker push $(TAG); \
				docker logout;
