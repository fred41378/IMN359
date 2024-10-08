import matplotlib.pyplot as plt
import numpy as np

k1 = 3
k2 = 1000
k3 = 100000

t = np.arange(-20.0, 20.0, 0.01)
s1 = 1 / 2
s2 = 1 / 2
s3 = 1 / 2

for n in range(1, k1):
    s1 += (2 * ((1 - np.cos(n * np.pi)) * np.cos(np.pi * n * t))) / (n ** 2 * np.pi ** 2)
for n in range(1, k2):
    s2 += (2 * ((1 - np.cos(n * np.pi)) * np.cos(np.pi * n * t))) / (n ** 2 * np.pi ** 2)
for n in range(1, k3):
    s3 += (2 * ((1 - np.cos(n * np.pi)) * np.cos(np.pi * n * t))) / (n ** 2 * np.pi ** 2)

plt.plot(t,t, 'r', linewidth=2)
plt.plot(t,s1, 'b')
plt.title('Nombre d\'harmonique n = {}'.format(k1))
plt.show()

plt.clf()
plt.plot(t,t, 'r', linewidth=2)
plt.plot(t,s2, 'g')
plt.title('Nombre d\'harmonique n = {}'.format(k2))
plt.show()

plt.clf()
plt.plot(t,t, 'r', linewidth=2)
plt.plot(t,s3, 'y')
plt.title('Nombre d\'harmonique n = {}'.format(k3))
plt.show()