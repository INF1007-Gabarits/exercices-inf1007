import numpy as np
import timeit

# Génération des tableaux
tableau1 = np.random.randint(1, 10, size=5)
tableau2 = np.random.randint(1, 100, size=1000000)

# Option 1 : Boucle `for`
def inverse_boucle(tableau):
    output = np.empty(len(tableau))
    for i in range(len(tableau)):
        output[i] = 1.0 / tableau[i]
    return output

# Option 2 : Opération vectorisée
def inverse_vectorisé(tableau):
    output = 1 / tableau
    return output

# Temps d'exécution pour chaque tableau et chaque option
time_loop_tableau1 = timeit.timeit(lambda: inverse_boucle(tableau1), number=1000)
time_vectorized_tableau1 = timeit.timeit(lambda: inverse_vectorisé(tableau1), number=1000)

time_loop_tableau2 = timeit.timeit(lambda: inverse_boucle(tableau2), number=10)  # (Moins d'itérations pour un grand tableau)
time_vectorized_tableau2 = timeit.timeit(lambda: inverse_vectorisé(tableau2), number=10)

# Affichage
print(f"Temps (Option 1 - boucle) pour tableau1: {time_loop_tableau1:.6f} s")
print(f"Temps (Option 2 - vectorisé) pour tableau1: {time_vectorized_tableau1:.6f} s")
print('-'*55)
print(f"Temps (Option 1 - boucle) pour tableau2: {time_loop_tableau2:.6f} s")
print(f"Temps (Option 2 - vectorisé) pour tableau2: {time_vectorized_tableau2:.6f} s")


