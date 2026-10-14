Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install test requirements


Connect your SGP4x sensor to a
`SensorBridge <https://sensirion.com/products/catalog/SEK-SensorBridge/>`_ on port 1. Assuming the SensorBridge is
attached to COM1 you can start the tests with the following command:

.. code-block:: bash

    pytest --serial-port=COM1                    # Run all tests for SGP4x on the sensor attached to COM1


.. note::
    The SensorBridge must have default settings (baudrate 460800, address 0)

In order to select tests for either SGP40 or SGP41, you can use the ``-m`` option of pytest:

.. code-block:: bash

    pytest --serial-port=COM1 -m "needs_sgp40 or not needs_device"         # Run only tests for SGP40
    pytest --serial-port=COM1 -m "needs_sgp41 or not needs_device"         # Run only tests for SGP41

