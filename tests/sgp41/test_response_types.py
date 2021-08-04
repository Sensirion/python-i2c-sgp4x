# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_i2c_sgp4x.sgp41.response_types import Sgp41SrawVoc, Sgp41SrawNox
import pytest


@pytest.mark.parametrize("value", [
    dict({'ticks': 25123}),
    dict({'ticks': 16345}),
])
def test_sraw_voc(value):
    """
    Test if the SGP41 SRAW VOC type works as expected for different values.
    """
    result = Sgp41SrawVoc(value.get('ticks'))
    assert type(result) is Sgp41SrawVoc
    assert type(result.ticks) is int
    assert result.ticks == value.get('ticks')


@pytest.mark.parametrize("value", [
    dict({'ticks': 31254}),
    dict({'ticks': 18246}),
])
def test_sraw_nox(value):
    """
    Test if the SGP41 SRAW NOx type works as expected for different values.
    """
    result = Sgp41SrawNox(value.get('ticks'))
    assert type(result) is Sgp41SrawNox
    assert type(result.ticks) is int
    assert result.ticks == value.get('ticks')
