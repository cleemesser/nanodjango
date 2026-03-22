====================
Playground embedding
====================

Saved scripts can be embedded in any webpage using a standard ``<iframe>``.


Getting the embed code
=======================

Open the script you want to embed, click **Share**, and choose your options. The
playground generates the ``<iframe>`` HTML for you to copy.

You can manually change the URL to deep link to a specific page in your script,
or add querystring parameters for your script to pick up. This
will automatically run the script, overriding the ``__autorun__`` setting.

Remember that your database isn't shared, and that if you set any environment variables
visitors will be prompted to provide their own values when they first run the script.
