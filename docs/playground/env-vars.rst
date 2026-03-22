================================
Playground environment variables
================================


What they are for
=================

Because :doc:`all saved scripts are public <usage>`, you should not put secrets such
as API keys, tokens or passwords directly in your code.

Intead, use the playground's environment variables to let your script read it from the
browser environment, and each person who runs the script supplies their own values.


How to use them
===============

When you open a script that declares environment variables, the playground prompts you
to enter values before running.

Your values are saved in your browser's local
storage - they stay on your machine and are never sent to the server.

You can update them at any time by clicking the **Env** button in the toolbar.

In your script, read the variable as you would any normal environment variable:

.. code-block:: python

    import os
    from nanodjango import Django

    app = Django()

    api_key = os.environ.get("OPENAI_API_KEY", "")


How long they last
==================

When entering values, you can choose how long they will be stored:

* **This session only** - they will be cleared when you close the tab
* **Remember in browser** - the browser will store the secrets for next time you visit
