'''
el usuario tiene que ingresar Nombre apellido edad y direccion, la edad tiene que ser un numeor entero 
luego mostrar con un print todos los datos de forma que se entienda bien
y mostrar en pantalla los valores de las varaibles y que tipo de dato son 
'''
nombre = input("Nombre: ")
apellido = input("apellido: ")
edad = int(input("Edad: "))
direccion = input("direccion: ")


print(nombre + " " + str(type(nombre)) + ' ' +apellido + str(type(apellido)) + ' ' +str(edad) + " " + str(type(edad)) + " " + direccion + '' + str(type(direccion)))