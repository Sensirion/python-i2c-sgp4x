#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from .version import version as __version__  # noqa: F401

from .sgp40.device import Sgp40I2cDevice  # noqa. F401
from .sgp41.device import Sgp41I2cDevice  # noqa. F401
