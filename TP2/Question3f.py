import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-25.0, 25.0, 0.01)
f1 = 0
f2 = 0
T = 20
w = 2 * np.pi / T
ordre_max = 10000


for n in range(-ordre_max,ordre_max):
    f1+=-(1/2)*np.sinc((np.pi*n)/2)*np.e**(1j*np.pi*n*t/10)

for n in range(-ordre_max, ordre_max):
    f2+=-(1/2)*np.sinc(w*n*5)*np.e**(1j*w*n*t)

plt.plot(t, f1, linewidth=7)
plt.plot(t, f2, linewidth=2)
plt.legend()
plt.show()

