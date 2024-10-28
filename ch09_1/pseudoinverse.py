# Exercice tiré de : https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.9-The-Moore-Penrose-Pseudoinverse/

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 1000)
x2_1 = -2*x1 + 2
x2_2 = 4*x1 + 8
x2_3 = -1*x1 + 2

plt.plot(x1, x2_1)
plt.plot(x1, x2_2)
plt.plot(x1, x2_3)
plt.xlim(-2., 1)
plt.ylim(1, 5)


A = np.array([[-2, -1], [4, -1], [-1, -1]])
A_plus = np.linalg.pinv(A)
b = np.array([[-2], [-8], [-2]])
res = A_plus.dot(b)
print(f'La solution du problème est x_1={round(res[0][0], 2)} et x_2={round(res[1][0], 2)}')

plt.scatter(res[0], res[1])

plt.show()