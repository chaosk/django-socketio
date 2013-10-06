How to test this project
========================


Prerequisites
-------------

- Using virtual environments is recommended, so create one.
- apt-get install firefox libevent-dev python-dev
- python setup.py develop
- pip install -r requirements-testing.pip


Unittests
---------

Unittests are run using the default Django command, so in your environment just run:

 - python django_socketio/example_project/manage.py test



BDDtests
--------

BDDtests are run using `py.test`_, and `pytest-bdd-splinter`_. Read more about creating BDDtests at the `pytest-bdd`_ github page.

You run them like this:

- python django_socketio/example_project/manage.py syncdb (only required once)
- python django_socketio/example_project/manage.py runserver_socketio (run in background by appending & if not using tmux/screen, make sure it's on port 9000)
- cd tests
- py.test


There are serveral debug options to py.test, here are a few:

- -x: stops on first failing test
- --pdb: drops to pdb when exception occures
- -k: specify test name, this will be the only test run


Feature files can be found in tests/features, and the test implementations in tests/functional. How these two are bound toghether will become clear once you read the `pytest-bdd`_ documentation.


Travis
------

The tests can also be run on Travis, as there is a .travis.yml available. Read the ci_build.sh file to learn more about the testing process there, Travis will invoke that file to test.


.. External references:
.. _py.test: http://pytest.org
.. _pytest-bdd: https://github.com/olegpidsadnyi/pytest-bdd
.. _pytest-bdd-splinter: https://github.com/olegpidsadnyi/pytest-bdd-splinter
