Testowanie funkcjonalności aplikacji webowej
===================

Projekt polega na przetestowaniu strony internetowej zrabatowani.pl:
- utworzenie testów automatycznych (python, selenium)
  ::

- umieszczenie projektu na github.com (system kontroli wersji)
  ::

- integracja projektu z TravisCi (Continuous Integration)
  ::

- integracja projektu z Docker (umieszczenie projektu na wirtualnym kontenerze)
  ::

- integracja projektu Heroku (Paas - hostowanie aplikacji na chmurze, Continuous Deployment - dostarczenie aplikacji do "klienta")

  ::


- Hermetyczne środowisko - pierwsza praca z projektem (virtualenv):

  ::

    source /usr/bin/virtualenvwrapper.sh
    mkvirtualenv mikroprojekt-selenium
    pip install -r requirements.txt
    pip install -r test_requirements.txt


- Aktywowanie hermetycznego środowiska dla aplikacji py (kontynuacja pracy):

  ::

    source /usr/bin/virtualenvwrapper.sh
    workon mikroprojekt-selenium


- Uruchamianie applikacji:

  ::

    python testy.py

- Status na TravisCi:

.. image:: https://travis-ci.org/elciak82/mikroprojekt-selenium.svg?branch=master
  :target:  https://travis-ci.org/elciak82/mikroprojekt-selenium



- Wykorzystanie platformy typu PaaS do hostowania aplikacji w chmurze (Heroku):

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
  :target: https://dashboard.heroku.com/apps/
