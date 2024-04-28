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

def plot(x, y):
	plt.title("Gráfica de e^(-x) * cos(2πx)")
	plt.plot(x, y, "--", color="orange")
	plt.xlabel("Valores de x")
	plt.ylabel("Valores de y")
	plt.grid()
	plt.show()

def get_data():
	x = np.linspace(-10, 5, 100)
	y = np.exp(-x) * np.cos(2 * np.pi * x)
	return x, y

def main():
	x, y= get_data()
	plot(x, y)

if __name__ == '__main__':
	main()
