
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def multiplicar(A,B):
    AB = [[0 for k in range(len(B[0]))] for j in range(len(A))]
    for i, row in enumerate(A):
        for j, col in enumerate([list(c) for c in zip(*B)]):
            AB[i][j] = sum([a*b for a, b in zip(row, col)])
    return AB

def column(matrix, i):
    return [row[i] for row in matrix]

def Markov(A,k):
    #Encontrar eigenvalores y eigenvectores
    eigenvalores, eigenvectores = np.linalg.eig(A)

    #Diagonalizacion
    Q=eigenvectores
    if(A.shape[1]==2):
        #print("2x2")
        D = np.array([[eigenvalores[0], 0],
                      [0, eigenvalores[1]]])
    if (A.shape[1] == 3):
        #print("4x4")
        D = np.array([[eigenvalores[0], 0, 0],
                      [0, eigenvalores[1], 0],
                      [0, 0, eigenvalores[2]]])
    if (A.shape[1] == 4):
        #print("4x4")
        D = np.array([[eigenvalores[0], 0, 0, 0],
                      [0, eigenvalores[1], 0, 0],
                      [0, 0, eigenvalores[2], 0],
                      [0, 0, 0, eigenvalores[3]]])
    Qinv=np.linalg.inv(Q)

    print("Q=\n" + str(Q))
    print("D=\n" + str(D))
    print("Qinv=\n" + str(Qinv))
    #Encobntrar P^k
    Dn=np.linalg.matrix_power(D, k)

    Resultado=multiplicar(multiplicar(Q,Dn),Qinv)
    columna = column(Resultado, 0)
    print("k="+str(k))
    for x in Resultado:
        print(x)


    if(A.shape[1]==2):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
    if (A.shape[1] == 3):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
        plt.plot(k, columna[2], 'go')
    if (A.shape[1] == 4):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
        plt.plot(k, columna[2], 'go')
        plt.plot(k, columna[3], 'yo')

############################################################################


#cantidad de iteraciones
k=20

#Matriz de transicion
A = np.array([[0.3, 0.5],
              [0.7, 0.5]])

B = np.array([[0.7, 0.1, 0.2],
              [0.2, 0.8, 0.1],
              [0.1, 0.1, 0.7]])

C = np.array([[0.2, 0.1, 0.4],
              [0.1, 0.5, 0.2],
              [0.7, 0.4, 0.4]])

D = np.array([[0.4, 0.1, 0.2, 0.1],
              [0, 0.1, 0.3, 0.3],
              [0.4, 0.7, 0.4, 0.4],
              [0.2, 0.1, 0.1, 0.2]])
############################################################################



for x in range(1, k):
    Markov(A, x)

plt.axis([0, k, -0.3, 1])
plt.savefig("graficaA.png")
plt.savefig("graficaA.png")
plt.show()

for x in range(1, k):
    Markov(B, x)
    
plt.axis([0, k, -0.3, 1])
plt.savefig("graficaB.png")
plt.savefig("graficaB.png")
plt.show()

for x in range(1, k):
    Markov(C, x)
    
plt.axis([0, k, -0.3, 1])
plt.savefig("graficaC.png")
plt.savefig("graficaC.png")
plt.show()

for x in range(1, k):
    Markov(D, x)
    
plt.axis([0, k, -0.3, 1])
plt.savefig("graficaD.png")
plt.savefig("graficaD.png")
plt.show()

print('\n------------------------------------------------------')  
print("EJERICIO 2:")
print('------------------------------------------------------\n') 
print("matriz A iteracion '4', matriz B iteracion '1', matriz C iteracion '4', matriz D iteracion '3'")