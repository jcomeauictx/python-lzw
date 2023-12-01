#!/usr/bin/python3
import sys, lzw
infile = lzw.readbytes('../lzw/card.lzw')
decompressor = lzw.decompress(infile)
for byte in decompressor:
    sys.stdout.buffer.write(byte)
