import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import ifft2, fftshift
from scipy.io import loadmat

#---a) IRM avec N lignes---
IRM = loadmat('IRM.mat')['IRM']
N = IRM.shape[0]

#-------------------------------------#
#---*** 0=lignes |*| 1=colonnes ***---#
#-------------------------------------#
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
    IRM_Modif = fftshift(IRM.copy())

    # Apply padding
    padded_matrix = np.pad(IRM_Modif,[((format-N)//2),((format-N)//2)],)
    print(padded_matrix.shape)
    plt.imshow(fftshift(np.log(np.abs(fftshift(ifft2(padded_matrix))))))
    plt.show()

zero_padding(600)
zero_padding(850)
zero_padding(1024)
#---d) échantillonage radial---

def echantillonnage_radial(angle):
    IRM_Modif = fftshift(IRM.copy())
    masque = np.zeros((N, N))
    taille_rayon = np.hypot(N, N)
    rayon = np.linspace(-taille_rayon, taille_rayon, int(taille_rayon)*4)

    nombre_lignes = 360 // angle
    angles = np.arange(nombre_lignes) * angle + (angle // 2)
    thetas = np.deg2rad(angles)

    rayon = rayon[:, np.newaxis]
    thetas = thetas[np.newaxis, :]

    x = np.round(N / 2 + rayon * np.cos(thetas)).astype(int)
    y = np.round(N / 2 + rayon * np.sin(thetas)).astype(int)

    coord_valide = (x > 0) & (x < N) & (y > 0) & (y < N)

    x_valide = x[coord_valide]
    y_valide = y[coord_valide]

    masque[x_valide, y_valide] = 1
    IRM_fenetre = IRM_Modif * masque
    IRM_fenetre_FFT = ifft2(IRM_fenetre)

    fig, ax = plt.subplots(1,3)
    ax[0].imshow(np.log(np.abs(ifft2(IRM_Modif))))
    ax[1].imshow(masque)
    ax[2].imshow(np.log(np.abs(IRM_fenetre_FFT)))
    plt.show()


echantillonnage_radial(10)
echantillonnage_radial(30)
echantillonnage_radial(70)
echantillonnage_radial(90)
echantillonnage_radial(180)
echantillonnage_radial(270)
echantillonnage_radial(360)


#---e) échantillonage aléatoire---

def echantillonnage_aleatoire(pourcentage):

    """Créer une matrice avec des nombre aléatoire de la taille de l'IRM
    Ensuite créer un masque où tout les nombres de la matrice aléatoire qui sont supperieur
    au pourcentage souhaité sont garder
    """
    IRM_copy = IRM.copy()
    matrice_random = np.random.rand(N, N) #Matrice de taille N avec des nombre aleatoire
    masque = matrice_random > (pourcentage / 100)  #Masque selon les critere voulu

    IRM_sampled = np.ones((N, N), dtype=complex)
    IRM_sampled[masque] = 0  # Mettre à zéro les points non sélectionnés

    image_reconstruite = IRM_copy*IRM_sampled #Reconstruction de l'image

    #Visualisation
    fig, ax = plt.subplots(1,2)
    ax[0].imshow(np.abs(IRM_sampled))
    ax[1].imshow(np.abs(ifft2(image_reconstruite)))
    fig.suptitle(f"{pourcentage}% de points utilisé")
    plt.show()


echantillonnage_aleatoire(30)
echantillonnage_aleatoire(60)
echantillonnage_aleatoire(90)