FROM python:2.7

ARG APP_DIR=/usr/src/testy

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD testy/ $APP_DIR/testy/
ADD testy/testy.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/testy \
    FLASK_APP=testy flask run --host=0.0.0.0
