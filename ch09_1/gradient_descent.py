import matplotlib
matplotlib.use('TkAgg')

import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Algorithme de minimisation
def minimisation(f, x0, k=0.01, n=5000):
    iteration_nb = 0
    x_courant = x0
    while iteration_nb < n:
        x_pre = x_courant
        gradient = f(x_courant+0.1) - f(x_courant)
        x_courant = x_courant - k * gradient
        iteration_nb += 1
    return x_courant

# Définition de la fonction à optimiser
f = lambda x: 6 * x*x + 4 * x + 12

# Optimisation en Python
x_min = minimisation(f, x0=0)
print(f'Python - valeur min : x={x_min} et f(x)={f(x_min)}')

# Optimisation avec Scipy
resultat = minimize(f, x0=0, method='CG', options={'maxiter':5000}, tol=1e-12)
print(f'Scipy - valeur min : x={resultat.x[0]} et f(x)={f(resultat.x[0])}')

# Affichage de la fonction et du résultat
x = np.linspace(-2, 1.5, 1000)
plt.figure()
plt.plot(x, f(x))
plt.plot(x_min, f(x_min), 'r.', ms=10)
plt.show()

# Calcul du temps de calcul
repeat = 10
number = 500
setup_p = ("from __main__ import f, minimisation")
times_p = timeit.repeat('minimisation(f, x0=0)', setup=setup_p, repeat=repeat, number=number)
print(f'Temps Python : {round(np.mean(times_p), 5)} secondes')
setup_s = ("from __main__ import f; from scipy.optimize import minimize")
times_s = timeit.repeat('minimize(f, x0=0, method=\'CG\', options={\'maxiter\':5000}, tol=1e-12)', setup=setup_s, repeat=repeat, number=number)
print(f'Temps Scipy : {round(np.mean(times_s), 5)} secondes')

