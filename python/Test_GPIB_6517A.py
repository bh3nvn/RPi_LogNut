#!/usr/bin/python2
# Test GPIB
import sys
import Gpib
instr = Gpib.Gpib(0,27)
instr.write("*IDN?")
print(instr.read())
