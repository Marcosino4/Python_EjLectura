import hashlib
import json

def registrar_usuario(usuarios):
    while True:
        nombre_usuario = input("Ingresa tu nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("El usuario ya existe. ¿Desea intentar con otro nombre de usuario?")
        else:
            break

    while True:
        contraseña = input("Ingresa una contraseña: ")
        confirmacion_contraseña = input("Confirma la contraseña: ")

        if contraseña == confirmacion_contraseña:
            hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
            usuarios[nombre_usuario] = hash_contraseña
            print("Usuario registrado con éxito.")
            break
        else:
            print("Las contraseñas no coinciden. Inténtalo de nuevo.")

def iniciar_sesion(usuarios):
    nombre_usuario = input("Ingresa tu nombre de usuario: ")

    if nombre_usuario in usuarios:
        contraseña = input("Ingresa tu contraseña: ")
        hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

        if hash_contraseña == usuarios[nombre_usuario]:
            print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(nombre_usuario))
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    else:
        print("El usuario no existe. ¿Quieres registrarte?")
        respuesta = input("Ingresa 's' para registrar o cualquier otra tecla para salir: ")
        if respuesta.lower() == 's':
            registrar_usuario(usuarios)

def borrar_usuario(usuarios):
    while True:
        nombre_usuario = input("Ingresa tu nombre de usuario: ")
        if nombre_usuario not in usuarios:
            print("El usuario no existe. ¿Desea intentar con otro nombre de usuario?")
        else:
            break

    while True:
        contraseña = input("Ingresa una contraseña: ")
        hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

        if hash_contraseña == usuarios[nombre_usuario]:
            del usuarios[nombre_usuario]
            print("Usuario {} borrado con éxito".format(nombre_usuario))
            break
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file)

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

usuarios = cargar_usuarios()

while True:
    print("\n1. Iniciar sesión")
    print("2. Crear usuario")
    print("3. Borrar usuario")
    print("4. Salir y guardar")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        iniciar_sesion(usuarios)
    elif opcion == '2':
        registrar_usuario(usuarios)
    elif opcion == '3':
        borrar_usuario(usuarios)
    elif opcion == '4':
        guardar_usuarios(usuarios)
        print("Usuarios guardados con éxito")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")