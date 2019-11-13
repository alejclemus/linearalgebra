import numpy as np
import sympy as sp
import time as tm


def ReglaCrammer(A,b):
    sol = []
    deta = round(np.linalg.det(A), 1)

    for i in range(len(b)):
        B = A.copy()
        B[:, i] = b
        detb = round(np.linalg.det(B), 1)
        sol.append(detb / deta)
    return sol


A = np.array([[1, 1, 0],
              [1, 0, 1],
             [0,  1, 0]])


b = np.array([[1,1,0,1],
             [1,0,1,0],
              [0,1,0,0],
              [0,1,0,0]])

                                          
b1= np.array([[1],
               [2],
               [4]])

b2= np.array([[1],
               [8],
               [4],
               [5]])

print("matriz A: \n" + str(A))
print("matriz B: \n" + str(b))

print('\n------------------------------------------------------')  
# Calcule los determinantes e inversas
print("EJERICIO 1:")
print('------------------------------------------------------\n') 
DETA = np.linalg.det(A)                             #det con numpy
print("Determinante A con numpy: \n " + str(DETA))
DETA2 = sp.Matrix(A).det()                          #det con sympy
print(" \n Determinante A con sympy: \n " + str(DETA2))

DETB = np.linalg.det(b)                             
print("Determinante B con numpy: \n " + str(DETB))
DETB2 = sp.Matrix(b).det()                          
print(" \n Determinante B con sympy: \n " + str(DETB2))

#calcular la inversa
inva = np.linalg.inv(A)                     #con numpy
print("inversa A con numpy: \n " + str(inva))
inva2 = sp.Matrix(A).inv()                  #con sympy
print("inversa A con sympy: \n " + str(inva2))

invb = np.linalg.pinv(b)                     
print("inversa B con numpy: \n " + str(invb))
invb2 = sp.Matrix(b).pinv()                  
print("inversa B con sympy: \n " + str(invb2))

print('\n------------------------------------------------------')  
print("EJERICIO 2:")
print('------------------------------------------------------\n') 
#solucion del sistema
print("A𝑥 = 𝑏1")

inicio=tm.time()
print(np.dot(inva, b1))
print("numpy: "+str(tm.time()-inicio))

inicio=tm.time()
print(np.dot(inva2, b1))
print("sympy: "+str(tm.time()-inicio))

inicio=tm.time()
print(ReglaCrammer(A, b1.transpose()))
print("cramer: "+str(tm.time()-inicio))

print("C𝑥 = 𝑏2")

print('\n------------------------------------------------------')  
print("EJERICIO 3:")
print('------------------------------------------------------\n') 

##c = np.random.randint(10,10, size=(100, 100)    
##d = np.random.randint(10,10, size=(100, 1)                
##print("matriz C: \n" + str(c))
##print("vector D: \n" + str(d))