#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing an existing class to alter its properties"""

import produce

class Apple(produce.Produce):
    """ Subclassing an existing class to modify it.

    Attributes:
        produce.Produce(class): Stored arrival time and shelf life of produce.

    Args:
        arrival(numeric): timestamp of when producte arrived.
        duration(numeric): The shelf life of produce.
    """
    duration = 5356800
