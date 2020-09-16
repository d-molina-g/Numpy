import numpy as np

a = np.array([1,2,3])
print("1D array:")
print(a,"\n")

b = np.array([(1,2,3,),(4,5,6),(7,8,9)])
print("2D array:")
print(b)

print(a[1]) #De esta manera acceder al dato (igual que un arreglo normal)

print(b[1,2]) #Se accede igual que una matriz bidimensional normal

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


#Crear una matriz de unos - 3 filas y 4 columnas
print("Función para rellenar Matriz sólo con unos")
unos = np.ones((3,4))
print(unos)

print("Función para rellenar Matriz sólo con ceros")
zeros = np.zeros((3,4))
print(zeros)

print(type(zeros[0][0])) #Los guarda como float

print("Función para rellenar Matriz con números random")
aleatorios = np.random.random((3,4))
print(aleatorios)

print("Función para rellenar Matriz vacia")
vacia = np.empty((3,4))
print(vacia)

print("Función para rellenar Matriz con un solo valor")
full = np.full((3,4),8)
print(full)

print("Función para rellenar Matriz con valores espaciados uniformemente")
espacio1 = np.arange(0,30,5) #Irá llenando desde 0 a 30, de 5 en 5.
print(espacio1)

espacio2 = np.linspace(0,2,5)
print(espacio2)

print("Función para crear una Matriz Identidad")
print("con np.eye")
identidad1 = np.eye(4,4) 
print(identidad1)
print("con np.identity()")
identidad2 = np.identity(4) 
print(identidad2)

#Conocer las Dimensiones de la Matriz
print("\n Imprime las dimensiones de una Matriz")
a=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a.ndim) #Imprime 2 (es una matriz 2d)

b=np.array([1,2,3])
print(b.ndim) #Imprime 1 (es un arreglo 1d)

#Conocer el tipo de datos
print("Para conocer el tipo de datos")
print(b.dtype) #En este caso int32 .. pero si no fueran consistentes todos los datos del arrelo arroja: U11

print("Tamaño y forma de una matriz")
print(a.size) #Para una matriz
print(b.size) #Para un arreglo

print(a.shape) #Para una matriz
print(b.shape) #Para un arreglo

print("Cambio de forma de una matriz")
x=np.array([(1,2,3),(4,5,6)]) #Matriz 2x3
print(x)
x=x.reshape(3,2)
print(x)

#Extraer los valores de todas las filas ubiados en la columna 3
print("Extracción de datos continuos de una fila por columna especifica")
print(x[0:,1])

print("Operaciones matematicas con Numpy en matrices")
print(a)
print(a.max())
print(a.min())
print(a.sum())
print(np.sqrt(a)) #Raiz cuadrada ... para cada elemento de la matriz
print(np.std(a)) #Desviación estandar

#Tambien se pueden hacer sumas, restas, divisiones, multiplicaciones de matrices
