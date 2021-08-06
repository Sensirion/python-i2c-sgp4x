# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_i2c_sgp4x.sgp40.response_types import Sgp40SrawVoc
import pytest


@pytest.mark.parametrize("value", [
    dict({'ticks': 25123}),
    dict({'ticks': 16345}),
])
def test_sraw_voc(value):
    """
    Test if SRAW VOC type works as expected for different tick values.
    """
    result = Sgp40SrawVoc(value.get('ticks'))
    assert type(result) is Sgp40SrawVoc
    assert type(result.ticks) is int
    assert result.ticks == value.get('ticks')
