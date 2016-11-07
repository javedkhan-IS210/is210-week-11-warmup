#!/usr/bin/ env python
# -*- coding: utf-8 -*-
""" Instanting and acessing custom class instances"""

import produce

TOMATO = produce.Produce()

EGGPLANT = produce.Produce(1311210802)

TOMATO_ARIVAL = TOMATO.arrival

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
