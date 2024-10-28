import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

# fréquence d’échantillonnage en Hz
fe = 100
# durée en seconde
T = 10
# Nombre de point :
N = T*fe
# Array temporel :
t = np.arange(1.,N)/fe
# fréquence du signal : Hz
f1, f2 = 0.5, 10
# signal temporel
sinus = np.sin(2*np.pi*f1*t) + 0.5 * np.sin(2**np.pi*f2*t)
# ajout de bruit
bruit = np.random.normal(0, 0.5, N-1)
sinus2 = sinus + bruit

# signal fréquentiel : on divise par la taille du vecteur pour normaliser la fft
fourier = fftpack.fft(sinus2)/np.size(sinus2)

# axe fréquentiel
axe_f = np.arange(0., N-1)*fe/N
demi_axe_f = axe_f[:len(axe_f)//2]

# Affichage de la figure
plt.figure()
plt.subplot(121)
plt.plot(t, sinus2, '-')
plt.plot(t, sinus, 'r-')
plt.xlabel('axe temporel, en seconde')
plt.subplot(122)
plt.plot(demi_axe_f, np.abs(fourier)[:len(demi_axe_f)], '-')
plt.xlabel('axe frequentiel en Hz')
plt.show()
