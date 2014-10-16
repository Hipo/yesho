Yesho - Display Model Properties in Django Admin
============

A reusable django app that displays model properties for superusers (or all users) in the Django Admin Panel. 

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install yesho

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/Hipo/yesho.git#egg=yesho

Add ``yesho`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'yesho',
    )

Add YeshoMixin to your ModelAdmins or extend your admin controllers from YeshoAdmin

.. code-block:: python

    from yesho.admin import YeshoMixin
    
    class MeetupAdmin(YeshoMixin, admin.ModelAdmin):
        search_fields = ("name", "body")
        ...

or 

.. code-block:: python

    from yesho.admin import YeshoAdmin
    
    class MeetupAdmin(YeshoAdmin):
        search_fields = ("name", "body")
        ...

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
