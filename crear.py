import time

print('Hola bienvenid@ a esto no es netflis')
time.sleep(1)
print('porfavor cree su usuario')

print()

crear = input()

print()
time.sleep(1)
print('Usuario creado')


time.sleep(1)
print()

print('Porfavor ingrese su usuario')
print()
usuario = input()

if usuario == str(crear):
	time.sleep(1)
	print('Bienvenido ' + crear)

else:
	time.sleep(1)
	print('este usuario no existe')