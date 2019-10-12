import numpy as np
import random

#Creacion de matrices con numpy
A = np.random.randint(-10,10, size=(15, 15))
B = np.random.randint(-10,10, size=(15, 15))
#matriz de 15x15 con valores enteros aleatorios de -10 a 10

print("matriz A: \n " + str(A))

print("matriz B: \n " + str(B))

l = random.sample(range(1,100), 25)
print("Diagonal A:")
np.fill_diagonal(A,l)
print("\n " + str(A))

print("Diagonal B:")
np.fill_diagonal(B,l)

#suma de matrices
print ("suma A+B \n " + str(A+B))

#producto de matrices
print("matriz A*B \n " + str(A*B))

#resta de matrices
print("matriz A-B  \n " + str(A-B))
print("matriz B-A  \n " + str(B-A))

print("A transpuesta \n " + str(A.transpose()))         #Transpuesta de Matriz
print("B transpuesta \n " + str(B.transpose()))         #Transpuesta de Matriz

c=np.random.randint(1,20,size=(1,20))
print("Vector c: \n " + str(c))
d=np.random.randint(1,20,size=(20,1))
print("Vector d: \n" + str(d))

print('Producto Punto')
print(np.dot(c,d))


