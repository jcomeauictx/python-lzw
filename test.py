#!/usr/bin/python3
import sys, lzw
with open('../lzw/card.lzw', 'rb') as infile:
    decompressor = lzw.decompress(infile)
    for byte in decompressor:
        sys.stdout.buffer.write(byte)
