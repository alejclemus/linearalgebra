import numpy as np
import matplotlib
matplotlib.use('TkAgg')            #usar esta linea solo en caso de que en computadoras Mac salga un error de: Python is not installed as a framework. The Mac OS X backend
import matplotlib.pyplot as plt


print('------------------------------------------------------')  
print("EJERICIO 1:")
print('------------------------------------------------------\n') 

#Resolucion de minimos cuadrados resolviendo la ec. normal (A^T)Ac =y
print('Minimos Cuadrados y Ecuaciones Normales')
A = np.array([[1,1920],
              [1,1930],
              [1,1940],
              [1,1950],
              [1,1960],
              [1,1970],
              [1,1980],
              [1,1990]])
b = np.array([[54.1],
              [59.7],
              [62.9],
              [68.2],
              [69.7],
              [70.8],
              [73.7],
              [75.4]])
print('A \n' + str(A) + '\n')
At=A.transpose()
#Ecuaciones Normales
AtA=np.dot(At, A)
Atb=np.dot(At, b)
print('At*A = \n' +str(AtA))
print('At*b = \n' +str(Atb))

#Solución Ecuacional Normal
print('AT Ax = ATb \n')
x = np.dot(np.linalg.inv(AtA),Atb)
print('Solución de mínimos cuadrados \n')
print(str(x) + '\n')

#Resolucion de minimos cuadrados usando np.linalg.lstsq

print('Recta de Mejor Ajuste')
x = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
y = np.array([54.1, 59.7, 62.9, 68.2, 69.7, 70.8, 73.7, 75.4])
A = np.vstack([x, np.ones(len(x))]).T           #Armar la matriz A con los puntos x y una columna de numeros 1
print('A \n' +str(A))
m, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('Los coeficientes de la recta de mejor ajuste son:')
print('pendiente = ', round(m,4), 'intersecto =', round(b,4), '\n')
plt.plot(x, y, 'o',label='Datos Actuales')
plt.plot(x, m*x + b,label='Recta Ajustada')
plt.plot(x,y-m*x-b,'x', label='Errores')
plt.plot(x,0*x,'--')
plt.title('Recta de Mejor Ajuste ')
plt.legend()
plt.savefig("Grafica1.png")
plt.show()
print("Esperanza de vida de las personas nacidas en el 2000:")
print(m*2000+b)

print('------------------------------------------------------')  
print("EJERICIO 2:")
print('------------------------------------------------------\n') 

#Resolucion de minimos cuadrados resolviendo la ec. normal (A^T)Ac =y
print('Minimos Cuadrados y Ecuaciones Normales')
A = np.matrix([[1,0.59],
              [1,0.8],
              [1,0.95],
              [1,0.45],
              [1,0.79],
              [1,0.99],
              [1,0.9],
              [1,0.65],
              [1,0.79],
              [1,0.69],
              [1,0.79],
              [1,0.49],
              [1,1.09],
              [1,0.95],
              [1,0.79],
              [1,0.65],
              [1,0.45],
              [1,0.6],
              [1,0.89],
              [1,0.79],
              [1,0.99],
              [1,0.85]])
b = np.matrix([[3980],
              [2200],
              [1850],
              [6100],
              [2100],
              [1700],
              [2000],
              [4200],
              [2440],
              [3300],
              [2300],
              [6000],
              [1190],
              [1960],
              [2760],
              [4330],
              [6960],
              [4160],
              [1990],
              [2860],
              [1920],
              [2160]])
print('A \n' + str(A) + '\n')
At=A.transpose()
#Ecuaciones Normales
AtA=np.dot(At, A)
Atb=np.dot(At, b)
print('At*A = \n' +str(AtA))
print('At*b = \n' +str(Atb))

#Solución Ecuacional Normal
print('AT Ax = ATb \n')
x = np.dot(np.linalg.inv(AtA),Atb)
print('Solución de mínimos cuadrados \n')
print(str(x) + '\n')

#Resolucion de minimos cuadrados usando np.linalg.lstsq

print('Recta de Mejor Ajuste')
l = []

for i in range(len(A.A1)):
  if i%2!=0:
    l.append(A.A1[i])
print(l)
x = np.array(l)
y = np.array(b.A1)
A = np.vstack([x, np.ones(len(x))]).T           #Armar la matriz A con los puntos x y una columna de numeros 1
#print('A \n' +str(A))
m, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('Los coeficientes de la recta de mejor ajuste son:')
print('pendiente = ', round(m,4), 'intersecto =', round(b,4), '\n')
plt.plot(x, y, 'o',label='Datos Actuales')
plt.plot(x, m*x + b,label='Recta Ajustada')
plt.plot(x,y-m*x-b,'x', label='Errores')
plt.plot(x,0*x,'--')
plt.title('Recta de Mejor Ajuste ')
plt.legend()
plt.savefig("Grafica2.png")
plt.show()