import os

ruta = r'D:\Python\Files'
ejecutables_escritorio = os.listdir(ruta)
archivos = []
directorios = []

for file in ejecutables_escritorio:
    nombre_archivo = os.path.join(ruta, file)
    if os.path.isfile(os.path.join(nombre_archivo)):
        archivos.append(file)
    elif os.path.isdir(nombre_archivo):
        directorios.append(file)

print("Archivos: ", archivos)
print("Directorios: ", directorios)
