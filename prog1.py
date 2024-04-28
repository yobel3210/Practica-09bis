#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog1.py
#
# Author: Yobel Dolores
# License: MIT
#
# Finds the largest number of those provided by the user
#
# ## ###############################################################
import sys
from math import sin

def read_int():
	try:
		s = input("int? ")
		n = int(s)
		return n
	except:
		return None

def main(argv):
	n = read_int()
	numbers = []
	while n:
		numbers.append(n)
		n = read_int()
	print("El elemento más pequeño es:", hex(min(numbers)) )

if __name__ == '__main__':
	main(sys.argv)
