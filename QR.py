from numpy import*

def traco(A):
    soma = 0
    for i in range(len(A)):
        soma+=A[i][i]
    return soma
	
def LeverrierFaddeev(A):
    tam = len(A)
    B = array(A)
    P = zeros(tam+1)
    P[0] = 1
    P[1] = -traco(B)
    for i in range(2,tam+1):
        B = dot(A, B + P[i-1]*identity(tam))
        P[i] = -traco(B/i)
    return P[::-1]
	
def matrizOrtogonal(A,i,j):
    U = identity(len(A))
    U[i][i] = A[0][0]/(math.sqrt(A[0][0]**2 + A[i][j]**2))
    U[j][j] = U[i][i]
    U[j][i] = A[i][j]/(math.sqrt(A[0][0]**2 + A[i][j]**2))
    U[i][j] =  -U[j][i]
    return U

def maiorElemento(A):
    for i in range(1,len(A)):
    	for j in range(i):
    		if abs(A[i][j]) > 0.0001:
    			return 1
    return 0

def QR(A):
    cont = 0
    tam = len(A)
    while maiorElemento(A) and cont<1000:
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
    return [A[i][i] for i in range(tam)]


git