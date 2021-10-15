Quick Start
===========

SensorBridge Example
--------------------

Following example code shows how to use this driver with a Sensirion SGP40/SGP41
connected to the computer using a `Sensirion SEK-SensorBridge`_. The driver
for the SensorBridge and the base SHDLC driver used in the example can be installed with

.. sourcecode:: bash

    pip install python-i2c-sgp4x[example]

.. _Sensirion SEK-SensorBridge: https://www.sensirion.com/sensorbridge/

SGP40
~~~~~

.. literalinclude:: ../example_sensorbridge_sgp40.py
    :language: python


SGP41
~~~~~

.. literalinclude:: ../example_sensorbridge_sgp41.py
    :language: python


Linux I²C Hardware
------------------

The following examples show how to use the SGP40 and SGP41 sensors with a generic Linux I²C hardware
(e.g. attached to the Raspberry Pi I²C port 1)


SGP40
~~~~~

.. literalinclude:: ../example_linux_sgp40.py
    :language: python


SGP41
~~~~~

.. literalinclude:: ../example_linux_sgp41.py
    :language: python
