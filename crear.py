import time
from os import system

usuarios = []


def usuario_nuevo():
    global usuarios
    system("cls")
    usuario = input('Por favor cree otro usuario: ')

    if usuario in usuarios:
        print("Este usuario ya existe, intenta de nuevo")
        time.sleep(1)
        usuario_nuevo()
    else:
        time.sleep(1)
        print('\nUsuario creado\n')
        usuarios.append(usuario)
        time.sleep(1)


print('Hola bienvenid@ a esto no es netflis')

time.sleep(1)

usuario = input('Por favor cree su usuario: ')
usuarios.append(usuario)

time.sleep(1)

print('\nUsuario creado\n')

time.sleep(1)

while True:
    print("¿Desea agregar otro usuario?: ")
    print("\n[SI] | [NO]\n")
    opc = input("Opción: ").upper()

    if opc == "SI":
        usuario_nuevo()
    elif opc == "NO":
        system("cls")
        break
    else:
        print("Opción invalida, intenta de nuevo.")
        time.sleep(1)
        system("cls")

comprobar = input("Ingresa tu usuario: ")

if comprobar in usuarios:
    print(f"Bienvenido {comprobar}.")
else:
    print(f"El usuario \"{comprobar}\" no existe.")
