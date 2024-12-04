import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.fft import fft, fftshift, ifft, ifft2, fftfreq



#Variables
sigma = 6
N = 1024
t = np.linspace(-512, 512,N)
dt = t[1] - t[0]
f = fftfreq(N, float(dt))

#---Question 1 a)---
gauss = np.exp(-t**2/(2*sigma**2)) #Creation de la Gaussiene en 1D
#Visualisation
plt.title("a) Gaussienne 1D ")
plt.plot(t,gauss)
plt.show()


Gauss = np.sqrt(2*(sigma**2)*np.pi)*np.exp(-2*(np.pi**2)*(sigma**2)*(f**2)) #Création théorique de la TF de la Gaussienne 1D
#Visualisation
plt.title("a) TF de Gaussienne 1D calculée théoriquement")
plt.plot(fftshift(Gauss))
plt.show()


#---Question 1 b)---
GaussFFT = fft(gauss) * dt #Création numérique de la TF de la Gaussienne 1D
#Visualisation
plt.title("b) TF de Gaussienne 1D calculée numériquement")
plt.plot(np.abs(fftshift(GaussFFT)))
plt.show()


#---Question 1 c)---
piece_regular = loadmat("piece-regular.mat")['x0'] #Chargement du piece regular
piece_regular.squeeze()
piece_regular_bruit = piece_regular + np.random.rand(N,1)*0.1 #Ajout du bruit
#Visualisation
fig, ax = plt.subplots(2)
fig.suptitle("c) piece regular")
ax[0].plot(t,piece_regular)
ax[1].plot(t,piece_regular_bruit)
plt.show()

#---Question 1 d)---
#--i.
#Visualisation
p_conv = np.convolve(piece_regular_bruit.squeeze(),gauss, 'same') #Convolution du piece regular bruité
plt.title("d) i. convolution du piece regular bruité")
plt.plot(p_conv)
plt.show()

#--ii.
piece_regularFFt = fft(piece_regular_bruit.squeeze()) #Création de la FFT du piece regular
#Visualisation
plt.title("d) ii. FFT du piece regular")
plt.plot(np.abs(fftshift(piece_regularFFt)))
plt.show()

produit_FFT = piece_regularFFt * GaussFFT #Multiplication des deux FFT
produit_FFT_inv = ifft(produit_FFT) #FFT inverse du produit
#Visualisation
plt.title("d) ii. Produit des TFs")
plt.plot(np.abs(fftshift(produit_FFT_inv)))
plt.show()

#--iii.
#Visualisation
fig, ax = plt.subplots(3)
fig.suptitle("c) piece regular")
ax[0].plot(np.abs(produit_FFT_inv), label="produit des transformées")
ax[1].plot(np.abs(fftshift(produit_FFT_inv)), label="produit des transformées inversé")
ax[2].plot(p_conv, label="convolution")
plt.show()

print('On remarque que la multiplication des transformées Fourier donne une convolution qui est symétriquement inversé.')

#--iv.