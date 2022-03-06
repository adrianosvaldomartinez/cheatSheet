class Employee:
#  __init__ es el metodo constructor de python LOS metodos especiales tienen los underscores
# como en cualquier otro consuctor aqui debemso pasarle las propiedades y metodos mutables de instancia
# SELF es un parametro que solo se usa dentro de la clase y hace referencia a la instacia
  def __init__(self, name):
    self.name = name
#  Debemos hacer disponible SELF para poder hacer referencia a la instancia inicializada de la clase
  def __repr__(self):
    return self.name
 
# en Python no se usa la palabra NEW, para inciar una instancia
# directamente asignamos al nombre de la clase y los parametros si corresponde
john = Employee('John')
print(john) # John

# inheritance
# para que una clase hija tengo todos los metodos y propiedades de una clase padre
# si queremos hacer una clase hija de otra se hace de la sigueinte manera

class Animal:
    planet= "earth"
    
# en python no se usa la palabra la extends simplemente se pasa como parametro la clase de la que quermeos que herede
class Dog (Animal):
    numberofLegs =4

# una vez mas, no usamos new, simplemente asignamos al nombre de la clase
firulais = Dog()
print(firulais.planet)
print(firulais.numberofLegs)