# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest

from sensirion_i2c_sgp4x.sgp40.response_types import Sgp40SrawVoc


@pytest.mark.needs_device
@pytest.mark.needs_sgp40
def test_measure_test(sgp40):
    """
    Run measure test and check if command works and responds with a successful test result
    """
    result = sgp40.measure_test()
    assert result == 0xD400, "Measure test failed with result 0x{:04X}".format(result)


@pytest.mark.needs_device
@pytest.mark.needs_sgp40
@pytest.mark.parametrize("relative_humidity,temperature",
                         [(50.0, 25.0),
                          (65.0, 23.5),
                          (62.0, 24.3)])
def test_measure_raw(sgp40, relative_humidity, temperature):
    """
    measure VOC raw signal
    """
    sraw_voc = sgp40.measure_raw(relative_humidity, temperature)
    assert type(sraw_voc) is Sgp40SrawVoc
    assert type(sraw_voc.ticks) is int


@pytest.mark.needs_device
@pytest.mark.needs_sgp40
def test_turn_heater_off(sgp40):
    """
    Test turn heater off and enter idle mode
    """
    sgp40.turn_heater_off()
