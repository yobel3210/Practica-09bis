#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog2.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# Plots the sin and cos functions
#
# ## ###############################################################
import numpy as np
import matplotlib.pyplot as plt

def plot(t, s, c):
	plt.title("Seno y coseno" )
	plt.plot(t, s, "-", color="orange")
	plt.plot(t, c, "b-")
	plt.legend(["y = cos(t)", "y = sin(t)"])
	plt.xlabel("Valores de t")
	plt.ylabel("Valores de y")
	plt.show()

def get_data():
	t = np.linspace(0, 4*np.pi, 100) # 0 a 12.64 / 100: 0, 0.1264, 0.2528 ... 12.64
	s = np.sin(t)
	c = np.cos(t)
	return t, s, c

def main():
	t, s, c = get_data()
	plot(t, s, c)

if __name__ == '__main__':
	main()
