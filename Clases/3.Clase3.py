#Programacion Orientada a objetos POO

class Animal:
    def __init__(self, name, edad, altura = 2.1):
        self.__name = name#propiedad privada
        self.edad = edad#propiedad publica
        self.altura = altura
        self.__nombreClase = 'Animal'
    
    #Metodos
    def hablar(self):
        print('AnimalHabla')

    def camianar(self):
        print('AnimalCamina')

    #SetGet
    def get_name(self):
        return self.__name
    
    def get_nombreClase(self):
        return self.__nombreClase
    
    def set_name(self, name):
        self.__name = name

    
class Perro(Animal):
    
    def __init__(self, name, edad, altura=2.1,raza = 'raza'):
        super().__init__(name, edad, altura)
        self.raza = raza

    def hablar(self):
        print('GUAUUUUUUU')
    pass

class Gato(Animal):
    def hablar(self):
        print('Miau')
    pass


myAnimal = Perro('MyAnimal',10, 1.1, "labrador")
myAnimal2 = Animal('MyAnimal',10, 1.1)
myAnimal3 = Gato('MyAnimal',10, 1.1)

myAnimalList = [myAnimal,myAnimal2,myAnimal3]


myAnimalList[0].hablar()
myAnimalList[1].hablar()
myAnimalList[2].hablar()

print(myAnimal.raza)

#myAnimal.edad = 20
#myAnimal.set_name("MyAnimalNuevo")
#myAnimal.hablar()
#myAnimal.camianar()

#print(myAnimal.get_name() + ' ' + str(myAnimal.edad) + ' ' + myAnimal.get_nombreClase() + " " + str(myAnimal.altura))


number_one, number_two = 5,1

number_two = '1'

print(number_one + number_two)
#try except
try:
    print('hola exe')
    print(number_one + number_two)
    print('No se a producido un error')
except:
    print('Se ha producido un error')






#try except else
#try:
 #   print(number_one + number_two)
  #  print('No se a producido un error')
#except:
   # print('Se ha producido un error')
#else:#solo se ejecuta si entre try y exect no se a producido un error 
    #print("La ejecucion continua correctamente")



    



