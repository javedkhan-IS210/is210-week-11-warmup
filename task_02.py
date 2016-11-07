#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a class"""

import time


class Snapshot(object):
    """ A class returning a time.

    Attributes:
        object: Returns Unix timestamp.
    """

    def __init__(self, created):
        """This is a constructor for snapshot class.

        Args:
            created(func): instance attribute of the time.time()

        Attributes:
            created(func): instance attribute of the time.time()
        """

        created = time.time()
        self.created = created
