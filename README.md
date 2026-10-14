# Python Driver for Sensirion I²C VOC and NOx Sensor

This repository contains the Python driver to communicate with Sensirion
VOC sensor SGP40 and VOC/NOx sensor SGP41 using the I²C interface. For details, please
read the [user manual](https://sensirion.github.io/python-i2c-sgp4x/).


## Supported Sensors

* SGP40
* SGP41

## Usage

The [User Manual](https://sensirion.github.io/python-i2c-sgp4x/) explains how to install the driver and documents it's API.

It also includes a [Quick-Start Guide]((https://sensirion.github.io/python-i2c-sgp4x/quickstart.html)) that shows how to execute first measurments using the included examples.


## SGP41 Conditioning

After each restart of the SGP41 sensor or when the hotplates have been switched off, the conditioning command must
be called from idle mode. The conditioning heats the hotplate of the NOx pixel to a different temperature compared
to the measurement mode enabling a faster switch-on thereafter.

It is recommended to execute the conditioning for 10s, but **10s must not be exceeded** to avoid damage to the sensing material.

## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-sgp4x/contributing.html)).



## License

See [LICENSE](LICENSE).
