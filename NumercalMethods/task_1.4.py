import numpy as np
import time
def decor(f):
    def wrapper(*args):
        start = time.time()
        print(f(*args))
        print("\nexecution time: ", round(time.time() - start, 10), '\n')
    return wrapper
@decor
def jacobi(A, b, N):
    x = np.zeros(len(b), float)
    for k in range(N):
        x_new = np.zeros(len(x), float)
        for i in range(len(A)):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        x = x_new
    return x
@decor
def jacobi_vector(A, b, N):
    x = np.zeros(len(b), float)
    D = np.diag(A)
    A_1 = A - np.diagflat(D)
    for i in range(N):
        x = (b - np.dot(A_1, x))/D
    return x
if __name__ == '__main__':
    A = np.array([[3,17,10],[2,4,-2],[6,18,-12]], float)
    b = np.array([1,3,5], float)
    N = 3
    jacobi(A, b, N)
    jacobi_vector(A, b, N)