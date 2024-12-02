import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import subplots
from scipy.io import loadmat
from plot_wavelet import plot_wavelet

lena = loadmat('lena2.mat')['lena']

lena_fwt_coef = (lena[::2,::] + lena[1::2,::])/np.sqrt(2)
lena_fwt_det = (lena[::2,::] - lena[1::2,::])/np.sqrt(2)
lena_fwt = np.concatenate((lena_fwt_coef, lena_fwt_det), axis=0)

energie_original = np.linalg.norm(lena)**2
energie_apres_reconstruction = np.linalg.norm(lena_fwt)**2
plot_wavelet(lena_fwt, 8)
plt.show()

lena_reconstruite = np.zeros_like(lena)
lena_reconstruite[::2,::] = lena_fwt_coef+lena_fwt_det
lena_reconstruite[1::2,::] = lena_fwt_coef-lena_fwt_det
fig, ax = plt.subplots(2)
fig.suptitle("Reconsctruction")
ax[0].imshow(lena_fwt, cmap='gray')
ax[1].imshow(lena_reconstruite, cmap='gray')
plt.show()

lena_fwt_coef2 = (lena_fwt[::,::2] + lena_fwt[::,1::2])/np.sqrt(2)
lena_fwt_det2 = (lena_fwt[::,::2] - lena_fwt[::,1::2])/np.sqrt(2)
lena_fwt2 = np.concatenate((lena_fwt_coef2, lena_fwt_det2), axis=1)
energie_original2 = np.linalg.norm(lena_fwt)**2
energie_apres_reconstruction2 = np.linalg.norm(lena_fwt2)**2

plot_wavelet(lena_fwt2, 8)
plt.show()

img = lena.copy()

Jmax = np.log2(16)-1
Jmin = 0
img_copy = img.copy()

for j in range(int(Jmax), Jmin-1, -1):
    img_a = img_copy[2**(int(j)+1):2**(int(j)+1):]
    Coarse1 = (img_a[::2,::] + img_a[1::2,::])/np.sqrt(2)
    Detail1 = (img_a[::2, ::] - img_a[1::2, ::])/np.sqrt(2)
    img_b = np.concatenate((Coarse1, Detail1), axis=0)
    Coarse1 = (img_b[::, ::2] + img_b[::, 1::2]) / np.sqrt(2)
    Detail1 = (img_b[::, ::2] - img_b[::, 1::2]) / np.sqrt(2)
    img_a = np.concatenate((Coarse1, Detail1), axis=1)
    img_copy[2**(j+1):2**(j+1):] = img_b
    j1 = int(Jmax) - j
    plot_wavelet(img_b, j1)
plt.show()
