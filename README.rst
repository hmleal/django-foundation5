============
Foundation 5
============

Django Foundation is a simple set of template tags that render forms in the
Foundation standard html.

Quick start
-----------

1. Add "foundation5" to your INSTALLED_APPS setting like this::

.. highlight:: python

::

   INSTALLED_APPS = (
       ...
       'foundation5',
   )

2. Include the foundation5 URLconf in your project urls.py like this::

.. highlight:: python

::

   url(r'^foundation/', include('foundation5.urls')),

3. Start the development server and visit http://127.0.0.1:8000/foundation to
   visit the demo.
