import numpy as np
import sympy as sp


# funcion para agregar la matriz aumentada a una matriz cualquiera (mxm)
def Aumentar(a):
    Valor = 'h' + str(sp.Matrix(a).shape)
    Identidad = sp.eye(int(Valor[2]))
    for x in range(0, int(Valor[2])):
        Identidad = Identidad.col_insert(x, sp.Matrix(a).col(x))
    return Identidad


# Escriba e imprima una matriz 2 x 2
A = np.array([[1, 2,0], [1, 0,1], [0,1,0]])
print("matriz A: \n" + str(A))

B = np.array([[2, 0,1], [1, 1,-4], [3,7,-3]])
print("matriz B: \n" + str(B))

C = np.array([[1, 1,0], [1, 0,1], [0,1,0], [1,2,3]])
print("matriz C: \n" + str(C))

print('\n------------------------------------------------------')  
# Calcule la inversa
print("EJERICIO 1:")
print('------------------------------------------------------\n') 
print("Inversa de la matriz A usando tres métodos: \n")
inva = np.linalg.inv(A)  # con numpy
print("\nnumpy: \n " + str(inva))
inva2 = sp.Matrix(A).inv()  # con sympy
print("\nsympy: \n " + str(inva2))
inva3 = Aumentar(A).rref()
print("\nFERR: \n " + str(inva3)+"\n")  # con FERR

print("Inversa de la matriz B usando tres métodos: \n")
invaB = np.linalg.inv(B)  # con numpy
print("\nnumpy: \n " + str(invaB))
invaB2 = sp.Matrix(B).inv()  # ccon sympy
print("\nsympy: \n " + str(invaB2))
invaB3 = Aumentar(B).rref()
print("\nFERR: \n " + str(invaB3)+"\n")  # con FERR

print("Pseudoinversa de la matriz rectangular C usando dos métodos: \n")
invaC = np.linalg.pinv(C)  # con numpy 
print("\nnumpy: \n " + str(invaC))
invaC2 = sp.Matrix(C).pinv()  # ccon sympy
print("\nsympy: \n " + str(invaC2)+"\n")
print('\n------------------------------------------------------')  

# Diferencia: con numpy la inversa se imprime

print("EJERICIO 2:")
print('------------------------------------------------------ \n')  
# Calcula el rango de las matrices
RangoA = np.linalg.matrix_rank(A)
print("rango A:\n"+str(RangoA))
RangoB = np.linalg.matrix_rank(B)
print("rango B:\n"+str(RangoB))
RangoC = np.linalg.matrix_rank(C)
print("rango C:\n"+str(RangoC))

print('\n------------------------------------------------------ ')  
print("EJERICIO 3:")
print('------------------------------------------------------ \n') 
NumcolsA = A.shape[1] #calcula numero de columnas
NumcolsB = B.shape[1]
NumcolsC = C.shape[1]
NulidadA = RangoA - NumcolsA
NulidadB = RangoB - NumcolsB
NulidadC = RangoC - NumcolsC
print("Nulidad A: " + str(NulidadA))
print("Base Espacio nulo A: \n" + str(sp.Matrix(A).nullspace())) # calcula una base para el espacio nulo 

print("Nulidad B: " + str(NulidadB))
print("Base Espacio nulo B: \n" + str(sp.Matrix(B).nullspace())) 

print("Nulidad C: " + str(NulidadC))
print("Base Espacio nulo B: \n" + str(sp.Matrix(C).nullspace())) 

