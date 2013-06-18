###################
django-runcommands
###################

.. image:: https://secure.travis-ci.org/magopian/django-runcommands.png?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/magopian/django-runcommands

runcommands: execute system commands from urls.

* Authors: Mathieu Agopian and `contributors
  <https://github.com/magopian/django-runcommands/contributors>`_
* Licence: BSD
* Compatibility: Django 1.4+, python2.7 and python3.3
* Project URL: https://github.com/magopian/django-runcommands
* Documentation: http://django-runcommands.rtfd.org/


Quickstart
==========

Install the application:

.. code-block:: sh

    pip install django-runcommands

And then add an entry for the runcommand's view in your URLCONF, for each
command you wish to make accessible:

.. code-block:: python

    # urls.py
    from runcommands.views import RunCommandView


    urlpatterns = patterns(
        '',
        url(r'^hello-world/$',
            RunCommandView.as_view(command='echo Hello World')),
    )

Your command output is now available at the url ``/hello-world/``.


Hacking
=======

Setup your environment:

::

    git clone https://github.com/magopian/django-runcommands.git
    cd django-runcommands

Hack and run the tests using `Tox <https://pypi.python.org/pypi/tox>`_ to test
on all the supported python and Django versions:

::

    make test
