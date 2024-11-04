import cmath as cm
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftshift, ifft, ifft2

k0= 4
N = 1000
t= np.linspace(0,1000,N)
y = np.cos(2*np.pi/ N * k0 * t)

#plt.plot(t, y, '-')
#plt.show()

G = fft(y)
f = np.linspace(-256, 256, N)

#plt.plot(f, np.real(G), '-')
#plt.show()

#plt.plot(f, np.real(fftshift(G)), '-')
#plt.show()

#no cos
G1 = np.zeros(N)
G1[k0]=N/2
G1[-k0]=N/2
y1 = ifft(G1)
plt.plot(t, np.real(y1), '-')
#plt.show()

G2 = np.zeros((N,N))
G2[0,k0] = N**2/2
G2[0,-k0] = N**2/2
y2 = ifft2(G2)
plt.imshow(np.real(y2), cmap='gray')
plt.savefig('test.png')
plt.show()
