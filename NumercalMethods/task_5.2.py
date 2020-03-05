import math

def S(f, l, m1, m2, h):
    N = int(l / h + 0.5)
    a = [0] * (N + 1)
    a[0] = m1
    a[N] = m2
    it = 0
    
    while True:
        xi = dict()
        th = dict()
        xi[1] = 0
        th[1] = m1
        
        for i in range(1, N):
            xi[i + 1] = 1 / (2 - xi[i])
            th[i + 1] = (-h * h * f(i * h, a[i]) + th[i]) / (2 - xi[i])
        U = [0] * (N + 1)
        U[N] = m2
        
        for i in reversed(range(0, N)):
            U[i] = xi[i + 1] * U[i + 1] + th[i + 1]
        if sum((U[i] - a[i]) * (U[i] - a[i]) for i in range(N + 1)) < 1e-9: 
            return U
        if it > 100: 
            return U
        it += 1
        a = U.copy()

solve = S(lambda xx, aa: -math.exp(aa), 1, 0, 0, 0.1)

print(solve)

for i in range(11):
    print("a(" + str(0.1 * i) + ") =", solve[i])