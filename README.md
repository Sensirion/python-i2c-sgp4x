# Python Driver for Sensirion I²C VOC and NOx Sensor

This repository contains the Python driver to communicate with Sensirion
VOC sensor SGP40 and VOC/NOx sensor SGP41 using the I²C interface. For details, please
read the [user manual](https://sensirion.github.io/python-i2c-sgp4x/).


## Supported Sensors

* SGP40
* SGP41

## Usage

See user manual at
[https://sensirion.github.io/python-i2c-sgp4x/](https://sensirion.github.io/python-i2c-sgp4x/).


## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]                       # Install requirements
pytest -m "not needs_device"                 # Run tests without hardware
pytest                                       # Run all tests
pytest -m "needs_sgp40 or not needs_device"  # Run all tests for sgp40
pytest -m "needs_sgp41 or not needs_device"  # Run all tests for sgp41
```

The tests with the marker `needs_sgp40` or `needs_sgp41` have following requirements:

- An SGP40 resp. SGP41 device must be connected to a
  [SensorBridge](https://www.sensirion.com/sensorbridge/) on port 1.
- Pass the serial port where the SensorBridge is connected with
  `--serial-port`, e.g. `pytest --serial-port=COM7`
- The SensorBridge must have default settings (baudrate 460800, address 0)


### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
python setup.py install                        # Install package
pip install -r docs/requirements.txt           # Install requirements
sphinx-versioning build docs docs/_build/html  # Build documentation
```

## License

See [LICENSE](LICENSE).
