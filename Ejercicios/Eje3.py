'''
pasos
    1 - ingresa una palabra
    2 - poner toda la palabra en minuscula
    3 - comprobar que la palabra este en minuscula y imprimir en terminal si efectivamente lo esta
    4 - mostrar los 2 primeros caracteres de la palabra
    5 - comprobar si la palabra arranca con "F" y postrar correcto o incorrecto
    6 - invertir la palabra y mostrar en pantalla
'''

texto = input("palabra: ")

print(texto.lower())

print(texto.lower().islower())

print(texto[0:2])

if "f" in str(texto):
    print("correcto")
else:
    print("incorrecto")

print(texto[::-1])