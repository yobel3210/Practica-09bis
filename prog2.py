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
	plt.title("Gráfica de y = 1/2 * x^2 + 1")
	plt.scatter(x, y, color="green", marker=".")
	plt.xlabel("Valores de x")
	plt.ylabel("Valores de y")
	plt.grid()
	plt.show()

def get_data():
	x = np.linspace(-10, 10, 100)
	y = 0.5 * x**2 + 1
	return x, y

def main():
	x, y= get_data()
	plot(x, y)

if __name__ == '__main__':
	main()
