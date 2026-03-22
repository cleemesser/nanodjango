===================
Playground packages
===================


Installing packages
===================

Enter one package name per line in the **Packages** field. Click
**Run** to install them and restart your script.


How packages are installed
===========================

The playground uses `Pyodide <https://pyodide.org>`_ - a WebAssembly build of Python
that runs in the browser. This means there are some limitations compared to a normal
Python environment:

**Packages must have a pure-Python wheel available.** Packages that include compiled C
extensions (native code) cannot be installed unless Pyodide ships a pre-compiled build
of them. Many popular packages like ``numpy``, ``pandas``, ``pillow``, and
``cryptography`` are pre-compiled by Pyodide and work fine. You can check the full list
of available packages in the
`Pyodide packages index <https://pyodide.org/en/stable/usage/packages-in-pyodide.html>`_.

**No packages that require network sockets at runtime.** The browser sandbox blocks
raw TCP/UDP connections, so packages that open network sockets
will not work. Some network connections are possible - Pyodide patches ``urllib.request``
to use the browser's fetch, or you could use
`pyodide.http <https://pyodide.org/en/stable/usage/api/python-api/http.html>`_.

**No system-level dependencies.** Packages that rely on shared libraries or system
binaries are not available.


Pre-installed packages
=======================

The following packages are already available without needing to add them to the
Packages field:

* ``django``
* ``nanodjango``
* ``django-ninja``
* ``pydantic``
* ``whitenoise``
* ``click``
* ``black``
* ``isort``
