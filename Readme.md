Installation
------------

``coinbase`` is available on `PYPI <https://pypi.python.org/pypi/coinbase/>`_.
Install with ``pip``:

.. code:: bash

    pip install coinbase

or with ``easy_install``:

.. code:: bash

    easy_install coinbase

The library is currently tested against Python versions 2.7 and 3.4+.

*Note*: this package name used to refer to the unofficial `coinbase_python`
library maintained by `George Sibble <https://github.com/sibblegp/>`_.
George graciously allowed us to use the name for this package instead. You can
still find that package `on Github <https://github.com/sibblegp/coinbase_python/>`_.
Thanks, George.

Documentation
-------------

The first thing you'll need to do is `sign up with Coinbase <https://coinbase.com>`_.

API Key + Secret
^^^^^^^^^^^^^^^^

If you're writing code for your own Coinbase account, `enable an API key <https://coinbase.com/settings/api>`_.

Next, create a ``Client`` object for interacting with the API:

.. code:: python

    from coinbase.wallet.client import Client
    client = Client(api_key, api_secret)
