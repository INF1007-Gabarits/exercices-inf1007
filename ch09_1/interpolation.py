import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.cos(x)

# Création des données initiales à partir de la fonction f avec un nombre fixe de points
n = 10
xp = np.linspace(0, 10.0, n)
yp = f(xp)

# Interpolation des données xp, yp avec un plus grand nombre de points
X = np.linspace(0, 10.0, 100)
p1 = interp.interp1d(xp, yp)
p3 = interp.interp1d(xp, yp, kind='cubic')

# Affichage de la figure
plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1)
plt.plot(xp, yp, 'or')
plt.plot(X, f(X), '-r', label='original')
plt.plot(X, p1(X), '-g',lw=2,label='lineaire')
plt.plot(X, p3(X), '-b',lw=2,label='cubique')
plt.legend(loc=0)
plt.subplot(1, 2, 2)
plt.plot(X, p1(X)-f(X), '-g', lw=2, label='lineaire')
plt.plot(X, p3(X)-f(X), '-b', lw=2, label='cubique')
plt.legend(loc=0)
plt.title('Erreur')
plt.show()