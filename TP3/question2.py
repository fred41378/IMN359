import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.fft import fft2, fft, fftshift, ifft, ifft2, fftfreq, ifftshift

lena = loadmat('lena.mat')['M'] #Chargement du fichier
N = lena.shape[0]
t = np.linspace(-np.pi, np.pi, N)

#---a) Création du filtre cosinus---
filtre_cos = 0.5 * np.cos(t) + 0.5

plt.plot(t, filtre_cos)
plt.show()

#---b) Création du filtre en 2D---
x = np.linspace(-np.pi, np.pi, N)
y = np.linspace(-np.pi, np.pi, N)
X,Y = np.meshgrid(x,y)

filtre_cos2D = (0.5 * np.cos(X) + 0.5)*(0.5 * np.cos(Y) + 0.5)
plt.imshow(filtre_cos2D, extent=(-np.pi, np.pi, -np.pi, np.pi))
plt.show()

#---c) Chargement de Lena et sa TF---

lenaFFT = fft2(lena) #Transformée du fichier
fig, ax = plt.subplots(2)
ax[0].imshow(lena)
ax[1].imshow(fftshift(np.log(np.abs(lenaFFT))))
plt.show()

#---d) Fenêtrage et sa transformée de fourier---
lena_fenetre = lena * filtre_cos2D
lena_fenetre_FFT = fft2(lena_fenetre)
fig, ax = plt.subplots(1,2)
ax[0].imshow(lena_fenetre)
ax[1].imshow(fftshift(np.log(np.abs(lena_fenetre_FFT))))
plt.suptitle('Fenêtrage de Lena et sa transformée de Fourier')
plt.savefig('question2d.png')
plt.show()

#---e) Filtre passe-bas---

lenaFFT_shift = fftshift(lenaFFT)
1
M1 = 64
M2 = 256
M3 = 360

masque1 = np.zeros_like(lenaFFT_shift)
masque2 = np.zeros_like(lenaFFT_shift)
masque3 = np.zeros_like(lenaFFT_shift)
masque1[N//2 - M1//2 : N//2  + M1//2, N//2  - M1//2 : N//2  + M1//2] = 1
masque2[N//2 - M2//2 : N//2  + M2//2, N//2  - M2//2 : N//2  + M2//2] = 1
masque3[N//2 - M3//2 : N//2  + M3//2, N//2  - M3//2 : N//2  + M3//2] = 1

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

pourcentage1 = np.round((M1/N)*100)
pourcentage2 = np.round((M2/N)*100)
pourcentage3 = np.round((M3/N)*100)

fig, ax = plt.subplots(1, 3)
fig.set_size_inches(10, 10)
fig.tight_layout(pad=1)
ax[0].imshow(np.real(lena_filtre1))
ax[0].set_title(f"{pourcentage1}% des points utilisé")
ax[1].imshow(np.real(lena_filtre2))
ax[1].set_title(f"{pourcentage2}% des points utilisé")
ax[2].imshow(np.real(lena_filtre3))
ax[2].set_title(f"{pourcentage3}% des points utilisé")
plt.show()