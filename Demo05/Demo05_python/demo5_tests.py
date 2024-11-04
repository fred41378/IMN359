from fileinput import lineno

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from scipy.fft import fft, fftshift, ifft


g = loadmat("piece_regular.mat")['piece_regular']
g = g.squeeze()
t = np.linspace(0, 1, np.shape(g)[0])
f = np.linspace(-256, 256, 512)
g += np.random.rand(len(f))*0.5
plt.plot(t, g, '-')
plt.show()

sigma=6
t1 = np.linspace(-30,30,100)
gauss = np.exp((-t1**2)/(2*sigma**2))
plt.plot(t1, gauss, '-')
plt.show()

g_conv = np.convolve(g, gauss,'same')
plt.plot(g_conv)
plt.show()

G = fft(g)
plt.plot(f, np.abs(fftshift(G)), '-')
plt.show()

Gauss = fft(gauss)
fgauss = np.linspace(-30, 30, 100)
plt.plot(fgauss, fftshift(np.abs(Gauss)), '-')
plt.show()

G_conv = fft(g_conv)
plt.plot(f, np.abs(fftshift(G_conv)), '-')
plt.show()

