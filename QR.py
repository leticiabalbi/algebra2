import numpy as np
import math
def matrizOrtogonal(A,i,j):
    U = np.identity(len(A))
    U[i][i] = A[j][j]/(math.sqrt(A[j][j]**2 + A[i][j]**2))
    U[j][j] = U[i][i]
    U[j][i] = A[i][j]/(math.sqrt(A[j][j]**2 + A[i][j]**2))
    U[i][j] =  -U[j][i]
    return U

def maiorElemento(A):
    elementos = np.zeros((len(A)**2-len(A))//2)
    aux = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i>j:
                elementos[aux] = A[i][j]
                aux= aux+1
    return elementos.max()

def QR(A,niter=1000,minimo = 0.000001):
    cont = 0
    Er = minimo+1
    while Er> minimo and cont<niter:
        R = np.identity(len(A))
        Q = np.identity(len(A))
        for i in range(len(A)):
            for j in range(len(A)):
                if i>j and A[i][j]!=0:
                    R = R.dot(matrizOrtogonal(A,i,j))
                    Q = Q.dot(matrizOrtogonal(A,i,j).transpose())
        R = R.dot(A)
        A = R.dot(Q)
        Er = maiorElemento(A)
        cont+=1
    return [A[i][i] for i in range(len(A))]