#Задача 5: Метод Зейделя

import numpy as np

def Metod(A, B, eps):
    x = np.array([0] * len(B))
    U = np.triu(A, k = 1)
    L = np.tril(A, k = -1)
    D = np.diagflat(np.diag(A)) 
    i = 0
    
    while True:
        y = np.dot(np.linalg.inv(L + D), np.dot(-U, x) + B)
        if (np.linalg.norm(x - y) < eps):
            return y
        x = y
        
        i += 1
        if (i > 200):
            return x
            
A = np.array([[1, 0.6, 0.01], [0.7, 1, 0.3], [0.7, 0.08, 1]])
B = np.array([1, 2, 1])
x = Metod(A, B, 1e-9)

print("reshenie:", x)
print("proverka:", np.linalg.norm(np.dot(A, x) - B))