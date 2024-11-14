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
n = 512 # size of mandrill
m = n / 2 # Number of coefficients in X and Y
F1 = np.zeros((n, n), dtype=complex)

sel = np.array([n / 2 - m / 2 , n / 2 + m / 2 + 1], dtype=int)+1
F1[sel[0]:sel[1],sel[1]] = lenaFFT[sel[0]:sel[1],sel[0]:sel[1]]

fig, axs = plt.subplots(1,2)
axs[0].imshow(np.log(np.abs(F1)), cmap='gray')
axs[0].set_title('Cropped spectrum : ' + str(m*m/(n*n)*100) + '% of coefficients')
axs[1].imshow(lena, cmap='gray')
axs[1].set_title('Original spectrum')
plt.savefig('mandrill_spectre.jpg')
plt.show()