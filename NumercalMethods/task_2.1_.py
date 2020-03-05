import numpy as np
def eigenValue(A, tol, max_it):
    q = np.zeros(len(A), float)
    q[0] = 1
    lyam_prev = np.dot(np.dot(A, q), q)
    lyam_ = 0
    it = 0
    while abs(lyam_- lyam_prev) > tol and it < max_it:
        q = np.dot(A,q) 
        q /= np.linalg.norm(q)
        lyam_prev = lyam_
        lyam_ = np.dot(np.dot(A, q), q)
        it += 1
    return lyam_, q, it
if __name__=='__main__':
    for n in range(2, 10):
        A = np.zeros((n,n), float)
        for i in range(0, n):
            for j in range(0, n):
                A[i, j] = 1.0/(i+j+1)
        tol, max_it = 0.001, 1000
        lyam_, q, it = eigenValue(A, tol, max_it)
        print("Eigen value: ", lyam_)
        print("Eigen vector: ", q)
        print("Count of iterations: ", it, '\n')
