MIKROPROJEKTY

- 1 selenium
- 2 integracja miniprojektu selenium z TravisCi, Heroku



- Aktywowanie hermetycznego środowiska dla aplikacji py:

  ::

    source /usr/bin/virtualenvwrapper.sh
    workon mikroprojekt-selenium


- Status na TravisCi:

.. image:: https://travis-ci.org/elciak82/mikroprojekt-selenium.svg?branch=master
  :target:  https://travis-ci.org/elciak82/mikroprojekt-selenium



- Wykorzystanie platformy typu PaaS do hostowania aplikacji w chmurze (zostala uzyta platforma Heroku)

  - w pliku requirements.txt zostal dodany gunicorn - szybszy od flaska, domyślnie jest w stanie obsłużyć więcej żądań od flask

  - został utworzony plik Procfile

  - w pliku runtime.txt zadano wersję Pythona, w której została stworzona aplikacja (python-2.7.14)

  ::

    heroku remote -v

  - add-commit-push do gita

  ::

    git push heroku master


- Status na Heroku:

.. image:: https://dashboard.heroku.com/apps/intense-wave-65690
  :target: https://dashboard.heroku.com/apps/intense-wave-65690
