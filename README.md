Flask jQuery AJAX Example (FJAE)
================================

Description
-----------
When the user selects an item from the vehicle "Make" drop down menu,
the vehicle "Model" drop down menu is populated by making an AJAX
request for a list of models for the make selected.

Install
-------

    $ virtualenv fjae
    $ source fjae/bin/activate
    $ pip install -r requirements.txt
    $ pip install -e ./

Run
---

    $ python bin/runserver.py

Go to http://localhost:5000 in your browser

Notes
-----

 - This was tested with Python 2.7.3 on Ubuntu 12.04.
 - I know Python better than I know JavaScript.

Relevant Documentation
----------------------

 - [Flask's "AJAX with jQuery"](http://flask.pocoo.org/docs/patterns/jquery/)
 - [Flask's MethodView class](http://flask.pocoo.org/docs/views/#method-based-dispatching)
 - [Flask's URL Routing](http://flask.pocoo.org/docs/api/#url-route-registrations)
 - [WTForms's Field class](http://wtforms.simplecodes.com/docs/1.0.2/fields.html#the-field-base-class)
 - [jQuery's .ajax() method](http://api.jquery.com/jQuery.ajax/)
