import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from scipy.io import loadmat
from scipy.fft import fft, fftshift, ifft, ifft2, fftfreq

N = 1024  # Nombre de points
f_cos = 5  # Fréquence centrale du filtre cosinus (en Hz)
dt = 0.01  # Intervalle de temps (en s)
t = np.linspace(0, N*dt, N)  # Vecteur temporel

# Création du filtre cosinus
filtre_cos = np.cos(2 * np.pi * f_cos * t)

plt.plot(t, filtre_cos)
plt.show()