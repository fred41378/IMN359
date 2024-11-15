import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.fft import fft2, fft, fftshift, ifft, ifft2, fftfreq, ifftshift

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
lena = loadmat('lena.mat')['M'] #Chargement du fichier
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

lenaFFT_shift = fftshift(lenaFFT)
centre = (N // 2, N // 2)

M1 = 64
M2 = 256
M3 = 360


masque1 = np.zeros_like(lenaFFT_shift)
masque2 = np.zeros_like(lenaFFT_shift)
masque3 = np.zeros_like(lenaFFT_shift)
masque1[centre[0] - M1//2 : centre[0] + M1//2, centre[1] - M1//2:centre[1] + M1//2] = 1
masque2[centre[0] - M2//2 : centre[0] + M2//2, centre[1] - M2//2:centre[1] + M2//2] = 1
masque3[centre[0] - M3//2 : centre[0] + M3//2, centre[1] - M3//2:centre[1] + M3//2] = 1

lenaFFT_centre1 = lenaFFT_shift * masque1
lenaFFT_centre2 = lenaFFT_shift * masque2
lenaFFT_centre3 = lenaFFT_shift * masque3

fig, ax = plt.subplots(1, 3)
ax[0].imshow(np.log(np.abs(lenaFFT_centre1) + 1))
ax[1].imshow(np.log(np.abs(lenaFFT_centre2) + 1))
ax[2].imshow(np.log(np.abs(lenaFFT_centre3) + 1))
plt.show()

#---f) Back shift de Lena---

lena_filtre1 = ifft2(ifftshift(lenaFFT_centre1))
lena_filtre2 = ifft2(ifftshift(lenaFFT_centre2))
lena_filtre3 = ifft2(ifftshift(lenaFFT_centre3))

fig, ax = plt.subplots(1, 3)
ax[0].imshow(np.real(lena_filtre1))
ax[1].imshow(np.real(lena_filtre2))
ax[2].imshow(np.real(lena_filtre3))
plt.show()