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


class usuario:
    def __init__(self, nombre, mail, clave):
        pass

class admin(usuario):
    def __init__(self, nombre, mail, clave):
        super().__init__(nombre, mail, clave)



myadmin = admin()
myUsers = [myadmin]

BD = {'Gonzalo':'123456'}

def Registro():
    a = True
    while(a):
        usuario = input("Usuario: ")
        if " " in usuario:
            print("Usuario no valido. No usar espacios")
        elif len(usuario) < 6:
            print("El nombre tiene que tener un minimo de 6 caracteres")
        elif usuario in BD:
            print("Usuario ya esta en uso")
        else:
            a = False
    b = True
    while(b):
        contraseña = input("Constraseña: ")
        if len(contraseña) < 4:
            print("La contraseña tiene que tener un minimo de 4 caracteres")
        else:
            b = False
    BD[usuario] = contraseña

def MostrarUsuarios():
    cantUsuarios = len(BD)
    if cantUsuarios > 0:
        for key, value in BD.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No hay ningun usuario registrado en este momento.")

def CambiarContraseña():
    print("Usuarios disponibles: ")
    for clave in BD.keys():
        print(clave)
    e = True
    while(e):
        selectContra = input("A que ususario queire cambiarle la contraseña: ")
        if selectContra in BD:
            f = True
            while(f):
                inputContra = input("Ingresar la contraseña: ")
                if inputContra == BD[selectContra]:
                    g = True
                    while(g):
                        newContra = input("Ingrese nueva contraseña: ")
                        if len(newContra) < 4:
                            print("La contraseña tiene que tener un minimo de 4 caracteres.")
                        else:
                            BD[selectContra] = newContra
                            print("La contraseña se a cambiado correctamente.")
                            g = False
                            f = False
                            e = False
                else:
                    print("Contraseña incorrecta.")
        else:
            print("El usuario ese no existe")

def QuitarUsuarios():
    c = True
    while(c):
        print("Usuarios disponibles: ")
        for clave in BD.keys():
            print(clave)
        select = input("Que ususario queire eliminar: ")
        d = True
        if select in BD:
            while(d):
                contCorrect = input("Ingresar la contraseña: ")
                if contCorrect == BD[select]:
                    BD.pop(select)
                    print(f"El usuario '{select}' se a eliminado")
                    d = False
                    c = False
                else:
                    print("La contraseña no es correcta.")
        else:
            print("Ese usuario ne existe")

def Main():
    h = True
    while(h):
        accion = input("Que quiere hacer. Escriba 'comandos' para ver comandos): ")
        if accion == "registros":
            Registro()

        elif accion == "mostrarUsuarios":
            MostrarUsuarios()
        
        elif accion == "cambiarContra":
            CambiarContraseña()

        elif accion == "quit":
            h = False
        
        elif accion == "comandos":
            print("Comandos admitidos: \n registros \n mostrarUsuarios \n quit \n quitarUsuario \n cambiarContra")

        elif accion == "quitarUsuario":
            QuitarUsuarios()

        else:
            print("El comando no es correcto. Para ver los comandos escriba: 'comandos'")


Main()
