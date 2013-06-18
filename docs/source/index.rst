Welcome to Django-runcommands documentation!
############################################

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
        url(r'^hello/$', RunCommandView.as_view(command='echo Hello World')),
        url(r'^top/$', RunCommandView.as_view(command='top -b -n1')),
    )

Your command outputs are now available at ``/hello/`` and ``/top/``.


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


Why
===

Have you every wanted to allow someone to simply run a command on your
production server, but without having to provide her with a ssh access, create
her a (restricted?) account, train her to connect using ssh...

Let's take a few use cases:

* deploy the latest version of the website: run a ``git pull``, send the HUP
  signal to gunicorn...
* get metrics from the server, the easy and simple way: ``du``, ``df``,
  ``who``, ``top -b -n1``...
* clean sessions, update cache
* plug a web hook (from github or bitbucket) to automatically do something on
  the server on each commit


Security
========

Yes, this is a potential security hole. If you configure a url that'll run ``rm
-rf``, you might have an issue on your hands.

In a more general way, if the command takes some time/cpu/memory, you'll
provide an easy way to an attacker to DOS your server.

You should definitely protect those urls, using decorators like
``login-required`` or ``permission_required``...
