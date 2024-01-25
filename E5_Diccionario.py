diccionario = {
    "nombre" : "",
    "apellido" : "",
    "edad" : ""
}
diccionario["nombre"] = input("Introduce tu nombre: ")
diccionario["apellido"] = input("Introduce tu apellido: ")
diccionario["edad"] = input("Introduce tu edad: ")

print(f"El usuario {diccionario["nombre"]} de apellido {diccionario["apellido"]} tiene {diccionario["edad"]} años")