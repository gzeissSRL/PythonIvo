'''
Un programa que te deje cargar usuarios en un sistema
poder ver esos usuarios y que el programa termine con un comando de texto

Condiciones de registro
    - No tener espacios el nombre
    - tener 6 o mas caracteres
    - Comprobar que el usuario no este registrado 
    Clave
        - minimo 4 caracteres
'''

BD = {'Gonzalo','123456'}

def Registro():
    
    print('registro')


def MostrarUsuarios():
    print('BD')


def Main():
    game = True
    while(game):
        accion = input("Que quiere hacer escriba 'Comandos' para ver comandos): ")
        if accion == "registros":
            Registro()

        elif accion == "mostrarUsuarios":
            MostrarUsuarios()
        
        elif accion == "quit":
            game = False

        elif accion == "comandos":
            print()
        else:
            print('Comando invalido')

Main()
