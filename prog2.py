#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog2.py
#
# Author: modified by: Yobel Dolores
# License: MIT
#
# Plots the sin and cos functions
#
# ## ###############################################################
import numpy as np
import matplotlib.pyplot as plt

def plot(t, s):
	plt.title("Gráfica de y = 1/2 * x^2 + 1")
	plt.scatter(t, s, color="green", marker=".")
	plt.xlabel("Valores de t")
	plt.ylabel("Valores de y")
	plt.grid()
	plt.show()

def get_data():
	t = np.linspace(-10, 10, 100) # 0 a 12.64 / 100: 0, 0.1264, 0.2528 ... 12.64
	s = 0.5 * t**2 + 1
	return t, s

def main():
	t, s= get_data()
	plot(t, s)

if __name__ == '__main__':
	main()
