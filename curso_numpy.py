import numpy as np

a = np.array([1,2,3])
print("1D array:")
print(a,"\n")

b = np.array([(1,2,3,),(4,5,6),(7,8,9)])
print("2D array:")
print(b)

print(a[2]) #De esta manera acceder al dato (igual que un arreglo normal)

print(b[2,2]) #Se accede igual que una matriz bidimensional normal

#Tipo de dato que nos retorna

print(type(a))
print(type(b))
print(type(np))
a=5
print(type(a))


#Verificar eficiencia en el almacenamiento de Numpy en comparación a Listas

import sys #Modulo para acceder a algunas variables usadas por el interprete
S=range(1000)
print("Resultado lista de Python:")
print(sys.getsizeof(5)*len(S))
print()
D=np.arange(1000)
print("Resultado Numpy array:")
print(D.size*D.itemsize)
#print(D.itemsize)


#Comprobar la eficiencia en Tiempo entre un arreglo normal (lista) vs Numpy array
##kjk

#comment

