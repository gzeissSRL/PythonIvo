#Clase 1 

#Print

print("Hola mundo") #Imprime un texto en la temrinal
print('chau')

#Comentarios

#Ejemplo comentario de una linea se usa "#"

'''
Comentario largo
1 
2
3
'''

#Tipos de datos

numero = 1
print(numero)
numero = 2
print(2)

variableINT = 1 #numero entero
print(type(variableINT))
varaibleFloat = 1.0 #numero con decimal
print(type(varaibleFloat))
variableString = "Hola" #Cadena de caracteres
print(type(variableString))
variableBool = True # Verdadero y falso 
print(type(variableBool))

#Operadores INT y float 

numero1 = 1
numero2 = 2

resultado = numero1 + numero2

print(resultado)

resultado = numero1 - numero2

print(resultado)

resultado = numero1 * numero2

print(resultado)

#Operador String

palabra1 = "Hola"
palabra2 = "mundo"

resultado = palabra1 + " " + palabra2

print(resultado)

#Operadores distintos tipos de datos

numero1 = 1.1
numero2 = 2

print(type(numero1))
print(type(numero2))

resultado = numero1 - numero2

print(type(resultado))
print(resultado)

#Convertir tipos de datos

numero1 = str(11)
print(type(numero1))
print(numero1)

#Propiedades 

nombre = 'casa'
print(len(nombre))#len cuenta el largo

nombre, apellido, apodo, edad = 'gonzalo', 'zeiss', 'gonza', 27

print(apellido)

print('Nombre: ' + nombre + " apellido: " + apellido)

# not and y or

print(3>2) 
print(3>4)

print(3>2 and 4>5)
print(3>2 or 4>5)
print(not(3>4))

#Input

nombre = input("Como te llamas?")
edad = int(input("Que edad tenes?"))
print(nombre)









