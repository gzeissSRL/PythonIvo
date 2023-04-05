'''
ingresa un texto, comproba si en el texto esta almenos una "a", si esta imprimi correcto si no imprimi incorrecto
despues pasa todo el texto a mayuscula y mostralo en terminal 
'''

texto = input("Texto: ")

if "a" in str(texto):
    print("correcto")
else:
    print("incorrecto")

if texto.count('a') > 0:
    print("correcto")
else:
    print("incorrecto")

print(texto.upper())