# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function


class Sgp41SrawVoc(object):
    """
    Represents a measurement response for the raw VOC signal.

    With the :py:attr:`ticks` you can access the raw data as received from the
    device.

    :param int ticks:
        The read ticks as received from the device.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.
        """

        #: The ticks (int) as received from the device.
        self.ticks = ticks

    def __str__(self):
        return '{:d}'.format(self.ticks)


class Sgp41SrawNox(object):
    """
    Represents a measurement response for the raw NOx signal.

    With the :py:attr:`ticks` you can access the raw data as received from the
    device.

    :param int ticks:
        The read ticks as received from the device.
    """
    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.
        """

        #: The ticks (int) as received from the device.
        self.ticks = ticks

    def __str__(self):
        return '{:d}'.format(self.ticks)
