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

#nombre = input("Como te llamas?")
#edad = int(input("Que edad tenes?"))
print(nombre)

nombre = 'hola'
print('tipo ' + str(type(nombre)) + 'tipo2' + str(type(nombre)))


#Funciones dentro de un string

texto = '\t En mi casa cae mucha \n nive en invierno'

print(texto)


#Formateo en strings

name, surname, age = 'Gonzalo', 'Zeiss', 35

#print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) 
#print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) #%s string %d entero %f float
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#Desempaquetado de caracteres 

name = 'python'

a, b ,c , e, f, g = name

print(b)

#Divicion

lenguage_slice = name[0:2]
print(lenguage_slice)

lenguage_slice = name[:: -1]
print(lenguage_slice)

lenguage = 'Python'

#print(lenguage.capitalize()) #primera letra en mayuscula
#print(lenguage.upper()) #Todo mayuscula
#print(lenguage.count('t')) #cantidad de un tipo
#print(lenguage.isnumeric()) #Es numerica
#print(lenguage.lower()) #minusculas
#print(lenguage.upper().isupper()) #mayuscula y compueba sie s mayuscula
#print(lenguage.startswith("Py")) #revisa como arranca

#IF 


confirmar = True

if confirmar:
    if 1>0.4:
        print('correcto2')
    else:
        print('incorrecto2')
    print('correcto')
elif 2> 3:
    print('incorrecto')
elif 5>2:
    print('a')

















