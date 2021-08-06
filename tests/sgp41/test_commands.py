# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest

from sensirion_i2c_sgp4x.sgp41.response_types import Sgp41SrawVoc, Sgp41SrawNox


@pytest.mark.needs_device
@pytest.mark.needs_sgp41
def test_get_serial_number(sgp41):
    """
    Get serial number and verify it is valid (non-zero)
    """
    serial_number = sgp41.get_serial_number()
    assert type(serial_number) is int
    assert serial_number != 0, "serial number can't be zero"


@pytest.mark.needs_device
@pytest.mark.needs_sgp41
def test_measure_test(sgp41):
    """
    Run measure test and check if command works and responds with a successful test result
    """
    result = sgp41.measure_test()
    assert result == 0xD400, "Measure test failed with result 0x{:04X}".format(result)


@pytest.mark.needs_device
@pytest.mark.needs_sgp41
def test_conditioning(sgp41):
    """
    only measure VOC values during conditioning
    """
    sraw_voc = sgp41.conditioning()
    assert type(sraw_voc) is Sgp41SrawVoc
    assert type(sraw_voc.ticks) is int


@pytest.mark.needs_device
@pytest.mark.needs_sgp41
@pytest.mark.parametrize("relative_humidity,temperature",
                         [(50.0, 25.0),
                          (65.0, 23.5),
                          (62.0, 24.3)])
def test_measure_raw(sgp41, relative_humidity, temperature):
    """
    measure VOC and NOx raw signals
    """
    sraw_voc, sraw_nox = sgp41.measure_raw(relative_humidity, temperature)
    assert type(sraw_voc) is Sgp41SrawVoc
    assert type(sraw_voc.ticks) is int
    assert type(sraw_nox) is Sgp41SrawNox
    assert type(sraw_nox.ticks) is int


@pytest.mark.needs_device
@pytest.mark.needs_sgp41
def test_turn_heater_off(sgp41):
    """
    Test turn heater off and enter idle mode
    """
    sgp41.turn_heater_off()
