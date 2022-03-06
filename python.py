from platform import python_branch


print("hola mundo")


# array en python
# casi no se usa, se tiene que importar un modulo
# tiene que ser del mismo tipo
from array import *

array1 = array('i', [10,20,30,40,50])
print (array1)

# lista en python, es lo mas flexible y mas usado
# puede tener difernte tipos
listaAlumnos = ["jose", "pepe", 1]

# tuple en python
# secuencia no  mutable
# es lo que retorna una funcion que retorna mas de un elemento
ordenllegadaCarrera =("schumager", "fitipaldi", "airtonsena")


# iteracion en pithon sobre una lista
for x in listaAlumnos:
    print(x)

# itera sobre os numero proveido menos el ultimo
for number in range (1,5):
    print (number)


# iterar sobre un diccionario 
# opcion uno iterear sobre las propiedades

file_counts = { "jpg" :10, "doc" : 15, "txt" :17 }

for extension in file_counts:
    print (extension)


# opcion 2 iterar sobre los valores y las propiedades
for ext, amount in file_counts.items():
    print (ext, amount)


print(file_counts.items())
print(file_counts.keys())
print(file_counts.values())


