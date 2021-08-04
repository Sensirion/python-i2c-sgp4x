# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, \
    SensorBridgeShdlcDevice, SensorBridgeI2cProxy
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_sgp4x import Sgp40I2cDevice, Sgp41I2cDevice
import pytest


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type="string")
    parser.addoption("--serial-bitrate", action="store", type="int",
                     default=460800)


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def _get_serial_bitrate(config):
    """
    Get the serial port bitrate to be used for the tests.
    """
    return config.getoption("--serial-bitrate")


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = [
        "SensorBridge serial port: " + str(_get_serial_port(config)),
        "SensorBridge serial bitrate: " + str(_get_serial_bitrate(config))
    ]
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def bridge(request):
    serial_port = _get_serial_port(request.config, validate=True)
    serial_bitrate = _get_serial_bitrate(request.config)
    with ShdlcSerialPort(serial_port, serial_bitrate) as port:
        dev = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
        yield dev


@pytest.fixture
def sgp40(bridge):
    # Configure SensorBridge port 1 for SGP40
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SGP40 device
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    sgp40 = Sgp40I2cDevice(I2cConnection(i2c_transceiver))

    yield sgp40

    # make sure the channel is powered off after executing tests
    bridge.switch_supply_off(SensorBridgePort.ONE)


@pytest.fixture
def sgp41(bridge):
    # Configure SensorBridge port 1 for SGP41
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SGP41 device
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    sgp41 = Sgp41I2cDevice(I2cConnection(i2c_transceiver))

    yield sgp41

    # make sure the channel is powered off after executing tests
    bridge.switch_supply_off(SensorBridgePort.ONE)
