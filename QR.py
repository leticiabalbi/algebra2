from numpy import*

def traco(A):
    soma = 0
    for i in range(len(A)):
        soma+=A[i][i]
    return soma
	
def LeverrierFaddeev(A):
    tam = len(A)
    B = array(A)
    S = zeros(((tam-1,tam,tam))) #tensor que guarda as matrizes B
    Q = zeros(tam+1)
    Q[0] = 1
    Q[1] = -traco(B)
    for i in range(2,tam+1):
        S[i-2] = B + Q[i-1] * identity(tam)
        B = dot(A, B + Q[i-1]*identity(tam))
        Q[i] = -traco(B/i)
    return Q[::-1], S

def autoVetores(A,av): #recebe uma matriz e o vetor dos autovalores
    tam = len(A) 
    I = identity(tam)
    U = zeros((tam,tam)) 
    V = zeros((tam,tam))
    B = LeverrierFaddeev(A)[1] #Recebe tensor com as matrizes B
    indice = 0    #indice atual
    cont = 0		#vezes que vai ser calculado
    U[0] = I[indice]  #recebe a primeira coluna da identidade
    for b in range(tam-1):   
        B[b] = B[b].T			#transpoe matriz
    while cont<tam:
        for i in range(1,tam):
            U[i] = av[cont] * U[i-1] + B[i-1][indice]   # recebe o autovetor atual vezes a coluna da identidade + a coluna do vetor B
        if all(U[i]==0):   #se o vetor for tudo 0
            indice += 1     #indice incrementa
            U[0] = I[indice]	#define uma nova coluna da indentidade
            cont = 0			#refaz os calculos
        else:				#senao
            V[cont] = U[i]   #matriz dos autovetores recebe o auto vetor calculado
            cont+=1  			# continua os calculos para o proximo auto valor
    return V 
	
def matrizOrtogonal(A,i,j):
    U = identity(len(A))
    U[i][i] = A[0][0]/(sqrt(A[0][0]**2 + A[i][j]**2))
    U[j][j] = U[i][i]
    U[j][i] = A[i][j]/(sqrt(A[0][0]**2 + A[i][j]**2))
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
        Q = identity(tam)
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