#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is the core of methallylescaline
# It is a crypto framework for obscurity ciphering.

# Author: Dan Zulla <dan@mescalin.co>
# (c) 2022 Some rights reversed.

import base64

from .strings import ascii

class methallylescaline:

    def __init__(self):
        pass

    # @credit: https://eddmann.com/
    def str_shift(*symbols):
        def _rot(n):
            encoded = ''.join(sy[n:] + sy[:n] for sy in symbols)
            lookup = str.maketrans(''.join(symbols), encoded)
            return lambda s: s.translate(lookup)
        return _rot
