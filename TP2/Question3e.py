import numpy as np

k1 = 3
k2 = 100
k3 = 10000
T = 2
w = 2 * np.pi / T

t = np.arange(-1.0, 1.0, 0.01)
s1 = 0
s2 = 0
s3 = 0

for n in range(-k1, k1):
    arg = n ** 2 * np.pi ** 2
    if arg != 0:
        s1 += (1/2)*((1 - np.cos(np.pi * n)) / arg) * np.exp(1j * w * n * t)
    else:
        s1 += 1 / 2
s1 = s1.real

for n in range(-k2, k2):
    arg = n ** 2 * np.pi ** 2
    if arg != 0:
        s2 += (1 / 2) * ((1 - np.cos(np.pi * n)) / arg) * np.exp(1j * w * n * t)
    else:
        s2 += 1 / 2
s2 = s2.real

for n in range(-k3, k3):
    arg = n ** 2 * np.pi ** 2
    if arg != 0:
        s3 += (1 / 2) * ((1 - np.cos(np.pi * n)) / arg) * np.exp(1j * w * n * t)
    else:
        s3 += 1 / 2
s3 = s3.real

err1 = np.mean((t - s1)**2)
print('Erreur quadratique numérique avec 3 harmoniques = {}'.format(err1))
err2 = np.mean((t - s2)**2)
print('Erreur quadratique numérique avec 100 harmoniques = {}'.format(err2))
err3 = np.mean((t - s3)**2)
print('Erreur quadratique numérique avec 10000 harmoniques = {}'.format(err3))
