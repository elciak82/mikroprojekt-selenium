# mikroprojekty

# 1 selenium
# 2 integracja miniprojektu selenium z TravisCi, Heroku

- Aktywowanie hermetycznego środowiska dla aplikacji py:

  ::

    source /usr/bin/virtualenvwrapper.sh
    workon wsb-simple-flask-app

status na TravisCi

.. image:: https://travis-ci.org/elciak82/mikroprojekt-selenium.svg?branch=master
    :target: https://travis-ci.org/elciak82/mikroprojekt-selenium


Wykorzystanie platformy typu PaaS do hostowania aplikacji w chmurze (zostala uzyta platforma Heroku)

- w pliku requirements.txt zostal dodany gunicorn - szybszy od flaska, domyślnie jest w stanie obsłużyć więcej żądań od flask

- został utworzony plik Procfile

- w pliku runtime.txt zadano wersję Pythona, w której została stworzona aplikacja (python-2.7.14)

Status na Heroku
