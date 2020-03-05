#Задача 1: Решение системы линейных уравнений с трехдиаго-нальной матрицей

import numpy as np

M = np.array([[23,123,0,0],[17,2,34,0],[0,231,78,22],[0,0,95,115]])
A = np.array([33,17,95,26])

def solve_lu(M,A):

	d = np.array([M[i,i] for i in range(len(M))],float)
	eu = np.array([M[i,i+1] for i in range(len(M)-1)],float)
	el = np.array([M[i+1,i] for i in range(len(M)-1)],float)
	a = np.zeros(len(M),float)
	a[1] = -eu[0]/d[0]

	for i in range(2,len(M)):
		a[i] = -eu[i-1]/(d[i-1]+el[i-1]*a[i-1])

	b = np.zeros(len(M),float)
	b[1] = A[0]/d[0]

	for i in range(2,len(M)):
		b[i] = (-el[i-1]*b[i-1] + A[i-1]) / (d[i-1] + el[i-1]*a[i-1])

	x = np.zeros(len(M),float)
	x[-1] = (-el[-1]*b[-1] + A[-1])/(d[-1] + el[-1]*a[-1])

	for i in range(len(M)-2,-1,-1):
		x[i] = a[i+1]*x[i+1] + b[i+1]
	return x
    
x = solve_lu(M,A)
print(np.dot(M,x))