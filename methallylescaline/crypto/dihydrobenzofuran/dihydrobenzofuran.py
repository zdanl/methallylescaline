#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a stateful encryption library for strings.

# Author: Dan Zulla <dan@mescalin.co>
# (c) 2022 Some rights reversed.

class Isopropylphenidate:

    def __init__(self, seed=[], auto_initialize=False):
        if auto_initialize is True:
            self.initialize()

    def _obtain_seed():
        # get 64 bytes of randomness from /dev/urandom
        pass

    def crypt(self, string=""):
        if len(string) == 0:
            return 1

        # convert a character to its unicode index point
        bin_array = [format(ord(char), "b") for char in string]
        return bin_array

    def initialize(self):
        if len(self.seed) > 0:
            self.srng = [random.random() for byte in range(1, 64)]
            print(self.srng)
