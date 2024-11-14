from distutils.util import Mixin2to3

import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from scipy.io import loadmat
from scipy.fft import fft2, fft, fftshift, ifft, ifft2, fftfreq

N = 512
t = np.linspace(-np.pi, np.pi, N)

#---a) Création du filtre cosinus---
filtre_cos = 0.5 * np.cos(t) + 0.5

plt.plot(t, filtre_cos)
plt.show()

#---b) Création ddu filtre en 2D---
x = np.linspace(-np.pi, np.pi, N)
y = np.linspace(-np.pi, np.pi, N)
X,Y = np.meshgrid(x,y)

filtre_cos2D = (0.5 * np.cos(X) + 0.5)*(0.5 * np.cos(Y) + 0.5)
plt.imshow(filtre_cos2D, extent=(-np.pi, np.pi, -np.pi, np.pi))
plt.show()

#---c) Chargement de Lena et sa TF---
lena = loadmat('lena.mat')['M'] #Chargement ddu fichier
lenaFFT = fft2(lena) #Transformée du fichier
fig, ax = plt.subplots(2)
ax[0].imshow(lena)
ax[1].imshow(fftshift(np.log(np.abs(lenaFFT))))
plt.show()

#---d) Fenêtrage et sa transformée de fourier---
lena_fenetre = lena * filtre_cos2D
lena_fenetre_FFT = ifft2(lena_fenetre)
fig, ax = plt.subplots(2)
ax[0].imshow(lena_fenetre)
ax[1].imshow(fftshift(np.log(np.abs(lena_fenetre_FFT))))
plt.show()

#---e) Filtre passe-bas---
M1 = 10
M2 = 1000
M3 = 3000
lenaFFTM1 = lenaFFT[-M1][M1]
lenaFFTM2 = lenaFFT[-M2][M2]
lenaFFTM3 = lenaFFT[-M3][M3]
plt.plot(lenaFFTM1)
plt.show()
