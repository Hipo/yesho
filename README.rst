Yesho - Display Model Properties in Django Admin
============

A reusable django app that displays model properties for superusers (or all users) in the Django Admin Panel. 

Installation
------------

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

After extending your admin class from YeshoAdmin or mixed it with YeshoMixin,
you will have some controls on the behaviour.

Example:

.. code-block:: python

    from yesho.admin import YeshoMixin

    class MeetupAdmin(YeshoMixin, admin.ModelAdmin):

        display_properties_button_label = "Display all properties of the model"

        on_demand_display_template = "yesho/on_demand_display.html"
        change_form_template = "yesho/change_form.html"

        excluded_properties = None
        show_only_to_superusers = True


We believe that the most important variables are **excluded_properties** and **show_only_to_superusers**.

If you pass the list of the properties that you want to exclude from the list to the excluded_properties variable,
they won't be shown at the properties list. This is useful for very heavy properties that you don't want to see in this list.

The default of the **show_only_to_superusers** is True. This means that this button will only be shown to super users.
If you explicitly set to False, than every user will see the button.


To Do's
-------

We developed this package for django suit admin theme. Although we love django suit, it would be great
if you can help us in order to support django classic admin and django grapelli.
If you have any idea, do not hesitate to contact us through the issue tracker.