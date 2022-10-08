#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is Escalin. A utility to use the Methallylescaline framework.
# It is also a ritualistic psychedelic.

# Author: Dan Zulla <dan@mescalin.co>

# (c) Mescalin Semicondutor Ltd.
# (c) 2022 Some rights reversed.

from methallylescaline.crypto import tryptamin, phenylethylamin
from methallylescaline.crypto import dihydrobenzofuran, isopropylphenidate

def main():
    # 64 bytes as seed, taken from the Intel Microcode Decryptor and randomized
    # Python3 is unsigned integers. 0 - 2,147,483,647

    # TODO verify
    # For Instruction Set Randomization on x64 we need only 2 byte as this is
    # proclaimedly the maximum size of a processor opcode. 

    seed = [
        0x43111198, 0x71994491, 0xc9c0fbcf, 0xdeb5dba5, 0xbb56c25b, 0xaaf111f1,
        0x9f3f82a4, 0xbb1c5ed5, 0x4f07aa98, 0x22235b01, 0xfc3185be, 0xde0c7dc3,
        0xbbbe5d74, 0xaadeb1fe, 0x9fbda6a7, 0xaa9bf174, 0xe56b69c1, 0xef334786,
        0xeac19dc6, 0xde0ca1cc, 0xbbe92c6f, 0xaa7484aa, 0xfcb0a9dc, 0xccf988da,
        0x182e5152, 0xa844c66d, 0xee0327c8, 0xde597fc7, 0xcbe00bf3, 0xaaa79147,
        0xf6ca6351, 0xdd292967, 0x27333a85, 0x11ff2138, 0xee2c6dfc, 0xde380d13,
        0xcb0a7354, 0xaa6a0abb, 0xf1c2c92e, 0xee722c85, 0xa2bfe8a1, 0xa22a664b,
        0xee4b8b70, 0xde6c51a3, 0xaa92e819, 0xaa990624, 0xf40e3585, 0xff6aa070,
        0x11c44146, 0x11376ff8, 0xee48774c, 0xdeb0bcb5, 0x1a1c0cb3, 0xaad8aa4a,
        0xfb9cca4f, 0xff2e6ff3, 0x949f82ee, 0x652263ff, 0xedc87814,
        0xfabefffa, 0xa650aceb, 0xfef9a3f7, 0xff7178f2, 0xff12344f, 
    ]
    
    # this is an example of the phenylethylamin cryptor
    ethoxybenzaldehyde = phenylethylamin.Phenylethylamin(seed=seed, auto_initialize=True)
    crypted_string = ethoxybenzaldehyde.crypt_string("i am a sample string")


    # this is an example of the tryptamin cryptor
    acetoxybetanitrostyrene = tryptamin.Tryptamin(seed=seed, auto_initialize=True)
    life_of_an_elf = open("hello-world", "r").read() # not closing file handle
    crypted_byte_array = acetoxybetanitrostyrene.crypt_block(life_of_an_elf)

    # this is an example of the isopropylphenidate cryptor
    methylbenzeneacetate = isopropylphenidate.Isopropylphenidate()
    new_string = methylbenzeneacetate.encrypt("i am a sample string")

    # this is an example of the dihydrobenzofuran cryptor
    dimethoxyethoxyamphetamine = dihydrobenzofuran.Dihydrobenzofuran(seed=seed, auto_initalize=True)
    fuzzed_string = dimethoxyethoxyamphetamine.fuzz("i am a sample string")

if __name__ == "__main__":
    main()
