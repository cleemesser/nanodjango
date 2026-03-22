==================
Playground console
==================

The console panel displays the stdout/stderr output from your script, and lets you run
Python code interactively in the same environment.
You must click **Run** to start your script before the console becomes active.

Use the arrow keys to navigate through your command history.

Nanodjango will automatically create you a superuser - you can find the username and
password in the console logs.


NanodjangoClient
================

After your script runs, a ``NanodjangoClient`` instance is available in the console.
Use it to make HTTP requests directly to your Django app without going through the
browser.


Making a GET request
---------------------

.. code-block:: python

    r = NanodjangoClient().get("/")
    print(r.status_code)
    print(r.content)


Making a POST request
----------------------

.. code-block:: python

    r = NanodjangoClient().post("/api/items/", data={"name": "widget"})
    r.debug()


Available methods
------------------

.. list-table::
   :header-rows: 1

   * - Method
     - Signature
     - Description
   * - ``get``
     - ``get(path, query_params=None)``
     - Make a GET request
   * - ``post``
     - ``post(path, data=None, content_type=...)``
     - Make a POST request

``query_params`` is an optional ``dict`` of query string parameters.

``content_type`` defaults to ``"application/x-www-form-urlencoded"``. Pass
``"application/json"`` and a serialised JSON string as ``data`` for JSON requests.


The response object
--------------------

``NanodjangoClient`` calls return a ``NanodjangoResponse``:

.. list-table::
   :header-rows: 1

   * - Attribute / method
     - Description
   * - ``r.status_code``
     - Integer HTTP status code (eg ``200``)
   * - ``r.status``
     - Full status line (eg ``"200 OK"``)
   * - ``r.content``
     - Response body as a string
   * - ``r.headers``
     - Response headers as a dict
   * - ``r.debug()``
     - Print status, headers, and body
   * - ``r.as_dict()``
     - Return status, headers, and body as a dict
   * - ``r.as_json()``
     - Return the above as a JSON string


Accessing the nanodjango app
=============================

``app`` is your nanodjango ``Django`` instance - it is in scope in the console after
your script has run.

This means you can use ``app.manage()`` to run Django management commands:

.. code-block:: python

    app.manage(["createsuperuser", "--username", "admin", "--email", "a@example.com"])

Pass the command and its arguments as a list of strings, exactly as you would on the
command line.


Helper utilities
================

A small number of utility functions are available in the console environment:

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``ls(path="/")``
     - Print a tree of files and directories at ``path`` in the in-browser filesystem
