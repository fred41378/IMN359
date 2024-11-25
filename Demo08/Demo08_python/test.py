import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import subplots
from scipy.io import loadmat

from dct import dct
from idct import idct
from dct2 import dct2
from idct2 import idct2
from snr import snr

from scipy.fft import fft2, fftshift, ifftshift, ifft2, rfft


piece_regular = loadmat("piece-regular.mat")['x0']
N1 = piece_regular.shape[0]
M1 = int(N1/8)
piece_dct = dct(piece_regular)
zeros1D = np.zeros_like(piece_dct)

piece_dct[M1:N1-M1] = zeros1D[M1:N1-M1]
ipiece_regular = idct(piece_dct)
dct_local1D = np.zeros_like(piece_regular)

w = 32

for i in range(int(N1/w)):
    mini_dct = np.array([w*i,i*w+w])
    dct_local1D[mini_dct[0]:mini_dct[1]] = dct(piece_regular[mini_dct[0]: mini_dct[1]])

fig, ax = subplots(4,1)
ax[0].plot(piece_regular)
ax[1].plot(np.abs(piece_dct))
ax[2].plot(ipiece_regular)
ax[3].plot(np.abs(dct_local1D))
plt.show()


lena = loadmat('lena.mat')['M'] #Chargement du fichier
N = lena.shape[0]
M = int(N/8)
t = np.linspace(-np.pi, np.pi, N)
lenaFFT = fft2(lena)
lenaFFT_shift = fftshift(lenaFFT)

masque = np.zeros((N,N))
masque[N//2 - M//2 : N//2  + M//2, N//2  - M//2 : N//2  + M//2] = 1

lenaFFT_centre = lenaFFT_shift * masque

dct_lena = dct2(lena)
fig, ax = plt.subplots(2, 1)
ax[0].imshow(np.log(np.abs(dct_lena)))
ax[1].imshow(np.log(np.abs(lenaFFT_shift)))
plt.show()

zero2D = np.zeros((N,N))
zero2D[0:M, 0:M] = dct_lena[0:M, 0:M]
zero2D = idct2(zero2D)

fig, ax = plt.subplots(2, 1)
ax[0].imshow(zero2D)
ax[0].set_title("DCT")
ax[1].imshow(np.abs(ifft2(lenaFFT_centre)))
ax[1].set_title("FFT")
plt.show()

dct_local2D = np.zeros((N,N))
