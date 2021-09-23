# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

from sensirion_i2c_driver import I2cDevice

from .commands import Sgp41I2cCmdExecuteConditioning, Sgp41I2cCmdMeasureRawSignals, \
    Sgp41I2cCmdExecuteSelfTest, Sgp41I2cCmdGetSerialNumber, Sgp41I2cCmdTurnHeaterOff


class Sgp41I2cDevice(I2cDevice):
    """
    SGP41 I²C device class to allow executing I²C commands.
    """

    def __init__(self, connection, slave_address=0x59):
        """
        Constructs a new SGP41 I²C device.

        :param ~sensirion_i2c_driver.connection.I2cConnection connection:
            The I²C connection to use for communication.
        :param byte slave_address:
            The I²C slave address, defaults to 0x59.
        """
        super(Sgp41I2cDevice, self).__init__(connection, slave_address)

    def get_serial_number(self):
        """
        Get Serial Number

        :return: 48-bit serial number as int
        :rtype: int
        """
        word0, word1, word2 = self.execute(Sgp41I2cCmdGetSerialNumber())

        return word0 << 32 | word1 << 16 | word2

    def conditioning(self, relative_humidity=None, temperature=None):
        """
        This command starts the conditioning, i.e., the VOC pixel will be operated
        at the same temperature as it is by calling the measure_raw command
        while the NOx pixel will be operated at a different temperature for
        conditioning. This command returns only the measured raw signal of the VOC
        pixel SRAW_VOC

        :param relative_humidity: relative humidity in percent. Defaults to 50% RH
        :param temperature: temperature in degree celsius. Defaults to 25°C
        :return:
            - raw VOC signal (:py:class:`~sensirion_i2c_sgp4x.sgp41.response_types.Sgp41SrawVoc`)
        :rtype: tuple
        """

        if relative_humidity is None:
            rh_raw = 0x8000
        else:
            rh_raw = int(relative_humidity * 65535 / 100)
        if temperature is None:
            t_raw = 0x6666
        else:
            t_raw = int((temperature + 45) * 65535 / 175)

        return self.execute(Sgp41I2cCmdExecuteConditioning(rh_raw, t_raw))

    def measure_raw(self, relative_humidity=None, temperature=None):
        """
        Read raw VOC signal and raw NOx signal

        :param relative_humidity: relative humidity in percent. Defaults to 50% RH
        :param temperature: temperature in degree celsius. Defaults to 25°C
        :return:
            - raw VOC signal (:py:class:`~sensirion_i2c_sgp4x.sgp41.response_types.Sgp41SrawVoc`)
            - raw NOx signal (:py:class:`~sensirion_i2c_sgp4x.sgp41.response_types.Sgp41SrawNox`)
        :rtype: tuple
        """
        if relative_humidity is None:
            rh_raw = 0x8000
        else:
            rh_raw = int(relative_humidity * 65535 / 100)
        if temperature is None:
            t_raw = 0x6666
        else:
            t_raw = int((temperature + 45) * 65535 / 175)

        return self.execute(Sgp41I2cCmdMeasureRawSignals(rh_raw, t_raw))

    def turn_heater_off(self):
        """
        Turn Heater Off I²C Command

        This command turns the hotplate off and stops the measurement.
        Subsequently, the sensor enters the idle mode.
        """
        return self.execute(Sgp41I2cCmdTurnHeaterOff())

    def measure_test(self):
        """
        Measure Test

        This command triggers the built-in self-test checking for integrity of the
        hotplate and MOX material and returns the result of this test as 2 bytes

        :return: 0xD400: all tests passed successfully or 0x4B00: one or more tests have failed
        :rtype: uint16
        """
        return self.execute(Sgp41I2cCmdExecuteSelfTest())
