import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-20.0, 20.0, 0.01)
f1 = 1/2
f2 = 1/2
T = 2
w = 2 * np.pi / T
ordre_max = 100

for n in range(1, ordre_max):
    f1 += (2 * ((1-np.cos(n*np.pi))*np.cos(np.pi*n*t)))/(n**2*np.pi**2)
for n in range(1, ordre_max):
    f2 += ((2*(1-np.cos(np.pi*n)))/(n**2*np.pi**2))*np.e**(1j*w*n*t)

plt.plot(t, f1, linewidth=7, label='reelle')
plt.plot(t, f2, linewidth=2, label='complexe')
plt.legend()
plt.show()

