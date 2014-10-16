Yesho - Display Model Properties in Django Admin
============

A reusable django app that displays model properties for superusers (or all users) in the Django Admin Panel. Just add YeshoMixin to your ModelAdmins.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install yesho

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://.git#egg=yesho

TODO: Describe further installation steps (edit / remove the examples below):

Add ``yesho`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'yesho',
    )

Add the ``yesho`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^app-url/', include('yesho.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load yesho_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate yesho


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 yesho
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
