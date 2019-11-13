import numpy as np
import sympy as sp

A = np.array([[1,1,0],
             [1,0,1],
             [0,1,0]])

B = np.array([[2,0,1,1],
             [1,1,2,0],
             [3,7,-3,1],
             [1,2,0,1]])

C = np.array([[1,1,0,1],
             [1,0,1,0],
             [0,1,0,0],
             [0,1,0,0]])

#determinantes
DETA = np.linalg.det(A)                             #con numpy
DETA2 = sp.Matrix(A).det()                          #con sympy

print('\n------------------------------------------------------')  
print("EJERICIO 1:")
print('------------------------------------------------------\n') 

#Eigenvalores y Eigenvectores

#con numpy
EIG = np.linalg.eigvals(A)
print("Eigenvalores con numpy matriz A: \n " + str(EIG))
EIGV = np.linalg.eig(A)
print("Eigenvectores con numpy matriz A: \n " + str(EIGV))

EIGB = np.linalg.eigvals(B)
print("Eigenvalores con numpy matriz B: \n " + str(EIGB))
EIGVB = np.linalg.eig(B)
print("Eigenvectores con numpy matriz B: \n " + str(EIGVB))

EIGC = np.linalg.eigvals(C)
print("Eigenvalores con numpy matriz C: \n " + str(EIGC))
EIGVC = np.linalg.eig(C)
print("Eigenvectores con numpy matriz C: \n " + str(EIGVC))

#con sympy
EIG2 = sp.Matrix(A).eigenvals()
print("Eigenvalores con sympy matriz A: \n " + str(EIG2))
EIGV2 = sp.Matrix(A).eigenvects()
print("Eigenvectores con sympy Matriz A: \n " + str(EIGV2))

EIG2B = sp.Matrix(B).eigenvals()
print("Eigenvalores con sympy matriz B: \n " + str(EIG2B))
EIGV2B = sp.Matrix(B).eigenvects()
print("Eigenvectores con sympy Matriz B: \n " + str(EIGV2B))

EIG2C = sp.Matrix(C).eigenvals()
print("Eigenvalores con sympy matriz C: \n " + str(EIG2C))
EIGV2C = sp.Matrix(C).eigenvects()
print("Eigenvectores con sympy Matriz C: \n " + str(EIGV2C))

print('\n------------------------------------------------------')  
print("EJERICIO 2:")
print('------------------------------------------------------\n') 
print("Diferencia: Se utiliza mas memoria en tiempo de ejecucion utilizando Simpy. No opera algunas cosas, como la raíz cuadrada, sino que la deja representada para evitar perder la mayor cantidad de decimales posibles")


print('\n------------------------------------------------------')  
print("EJERICIO 3:")
print('------------------------------------------------------\n') 

DIAG = sp.Matrix(A).diagonalize()
print("Diagonalizacion con sympy matriz A: \n " + str(DIAG))

POL = sp.Matrix(A).charpoly()
print("Polinomio caracteristico matriz A: \n " + str(POL))

DIAGB = sp.Matrix(B).diagonalize()
print("Diagonalizacion con sympy matriz B: \n " + str(DIAGB))

POLB = sp.Matrix(B).charpoly()
print("Polinomio caracteristico matriz B: \n " + str(POLB))

DIAGC = sp.Matrix(C).diagonalize()
print("Diagonalizacion con sympy matriz C: \n " + str(DIAGC))

POLC = sp.Matrix(A).charpoly()
print("Polinomio caracteristico amtriz C: \n " + str(POLC))

print('\n------------------------------------------------------')  
print("EJERICIO 4:")
print('------------------------------------------------------\n') 


print("Eigenvectores con sympy Matriz A: \n " + str(EIGV2))
print("Eigenvectores con sympy Matriz B: \n " + str(EIGV2B))
print("Eigenvectores con sympy Matriz C: \n " + str(EIGV2C))

print('\n------------------------------------------------------')  
print("EJERICIO 5:")
print('------------------------------------------------------\n') 

inicio=tm.time()
EIGV2 = sp.Matrix(A).eigenvects()
print("sympy: "+str(tm.time()-inicio))

inicio=tm.time()
EIGV = np.linalg.eig(A)
print("numpy: "+str(tm.time()-inicio))

print("Numpy es mas rapido que Simpy")