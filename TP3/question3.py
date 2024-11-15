import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.io import loadmat
from scipy.fft import ifft2, fftshift


#---a) IRM avec N lignes---
IRM = loadmat('IRM.mat')['IRM']
N = IRM.shape[0]

#------------------------------------#
#---*** 0=lignes |*| 1=colonnes ***---#
#------------------------------------#
def imageSurN(N, direction):

    IRM_Modif = IRM.copy()
    if direction == 0:
        IRM_Modif[::N, :] = 0
    elif direction == 1:
        IRM_Modif[:,::N] = 0

    total_de_points = np.count_nonzero(IRM_Modif)
    pourcentage = (total_de_points / IRM_Modif.size) * 100

    IRM_IFFT = np.abs(ifft2(IRM_Modif))

    # Visualisation
    plt.imshow(IRM_IFFT)
    plt.title(f"{pourcentage:.2f}% des points utilisés")
    plt.show()

imageSurN(2,0)
imageSurN(3,0)
imageSurN(4,0)

#---b) IRM avec N colonnes---
imageSurN(2,1)
imageSurN(3,1)
imageSurN(4,1)

#---c) zero_padding---

def zero_padding(format):

    IRM_padded = np.zeros((format, format), dtype=complex)

    x = (format - IRM.shape[0]) // 2
    y = (format -  IRM.shape[0]) // 2

    IRM_padded[x:x + IRM.shape[0], y:y + IRM.shape[1]] = IRM

    IRM_IFFT = np.abs(ifft2(IRM_padded))

    # Visualisation
    plt.imshow(IRM_IFFT)
    plt.title(f"IRM reconstruite avec zero padding {format}x{format}")
    plt.show()

zero_padding(600)
zero_padding(850)
zero_padding(1024)

#---d) échantillonage radial---

#à l'aide

#---e) échantillonage aléatoire---

def echantillonRand(pourcentage):

    """Créer une matrice avec des nombre aléatoire de la taille de l'IRM
    Ensuite créer un masque où tout les nombres de la matrice aléatoire qui sont supperieur
    au pourcentage souhaité sont garder
    """
    matrice_random = np.random.rand(N, N) #Matrice de taille N avec des nombre aleatoire
    masque = matrice_random > (pourcentage / 100) #Masque selon les critere voulu


    IRM_sampled = IRM.copy()
    IRM_sampled[masque] = 0  # Mettre à zéro les points non sélectionnés

    image_reconstructed = np.abs(ifft2(IRM_sampled)) #Reconstruction de l'image

    #Visualisation
    plt.imshow(image_reconstructed)
    plt.title(f"{pourcentage}% des points utilisés")
    plt.show()

echantillonRand(30)
echantillonRand(60)
echantillonRand(90)