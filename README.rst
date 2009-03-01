==================
Django Quotes
==================

Django Quotes is a simple way to place random quotes in a website. Currently the quotes are stored in the app.

Features
========

* Simple Quotes model
* Template tag for pulling Quotes into templates

Installation
============

1. Add the ``quotes`` directory to your Python path.
2. Add ``quotes`` to your ``INSTALLED_APPS``.
3. Run the command ``manage.py syncdb`` to install the models.

Usage
=====

Once content is available in the `quotes` model, it can be accessed via
the templates using the provided template tags::

    {% load quote_tags %}
    <div class="hello">
        {% show_random_quote %}
    </div>

The above will gather the quotes from the model and then randomly display them one at a time.

