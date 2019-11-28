import numpy as np
import math
def matrizOrtogonal(A,i,j):
    U = np.identity(len(A))
    U[i][i] = A[0][0]/(math.sqrt(A[0][0]**2 + A[i][j]**2))
    U[j][j] = U[i][i]
    U[j][i] = A[i][j]/(math.sqrt(A[0][0]**2 + A[i][j]**2))
    U[i][j] =  -U[j][i]
    return U

def maiorElemento(A, tam):
    for i in range(1,tam):
    	for j in range(i):
    		if abs(A[i][j]) > 0.0001:
    			return 1
    return 0

def QR(A,tam):
    cont = 0
    while maiorElemento(A,tam) and cont<1000:
        Q = np.identity(tam)
        for i in range(1,tam):
            for j in range(i):
                if A[i][j]!=0:
                    U = matrizOrtogonal(A, i, j)
                    Q = dot(U,Q)
                    A = dot(U,A)
        
       	Q = Q.T
       	A = dot(A,Q)
        cont+=1
    return [A[i][i] for i in range(len(A))]