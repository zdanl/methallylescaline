#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a stateful encryption library.
# It is the second of two. 

# Author: Dan Zulla <dan@mescalin.co>
# (c) 2022 Some rights reversed.

class Tryptamin:

    seed = []
    srng = []

    def __init__(self, seed=[], auto_initialize=False):
        if auto_initialize is True:
            self.initialize()

    def _obtain_seed():
        # get 64 bytes of randomness from /dev/urandom
        pass

    def initialize(self):
        if len(self.seed) > 0:
            self.srng = [random.random() for byte in range(1, 64)]
