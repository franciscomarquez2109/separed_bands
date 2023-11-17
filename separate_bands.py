import os
import re
import shutil

# arreglo con las expresiones regulares
regularExpressions = [r'550nm',r'660nm',r'790nm',r'735nm']
# Directorio de origen donde se buscarán los archivos JPG
sourceDirectory = "."
# Directorio de destino donde se crearán las carpetas y se moverán los archivos
destinationDirectory = "./bandas"

# Crear directorio de destino si no existe
if not os.path.exists(destinationDirectory):
    os.makedirs(destinationDirectory)

# Obtener la lista de archivos JPG en el directorio de origen
tifFiles = [file for file in os.listdir(sourceDirectory) if file.lower().endswith('.tif')]

# Iterar sobre los archivos tif y moverlos a carpetas correspondientes
for file in tifFiles:
    #Iterar sobre las expresiones regulares para buscar cada una de ellas en la lista de bandas
    for expression in regularExpressions:
        rowExpression = re.compile(expression)
         # Buscar la coincidencia con la expresión regular en el nombre del archivo
        coincidences = rowExpression.findall(file)

        if len(coincidences) > 0:

            # asignamos el nombre de la banda que estamos buscando a la carpeta
            folderName = coincidences[0]

            # Crear directorio para el nombre si no existe
            diretoryName = os.path.join(destinationDirectory, folderName)
            if not os.path.exists(diretoryName):
                os.makedirs(diretoryName)

            # Ruta completa del archivo de origen y destino
            originRoute = os.path.join(sourceDirectory, file)
            destinationRoute = os.path.join(folderName, file)

            # copiar el archivo a la carpeta correspondiente
            shutil.copy(originRoute, destinationRoute)
            print(f"Copiando '{file}' a '{diretoryName}'")
            break

#obtenemos la lista de imagenes jpg para agregarlas a una carpeta en el mismo destino
files_jpg = [file for file in os.listdir(sourceDirectory) if file.lower().endswith('.jpg')]

# nombre unico para la carpeta de imagenes
folderName = 'RGB'

 # Crear directorio para el nombre si no existe
diretoryName = os.path.join(destinationDirectory, folderName)
if not os.path.exists(diretoryName):
    os.makedirs(diretoryName)

# Iterar sobre los archivos JPG y moverlos a carpetas correspondientes
for file in files_jpg:
   
    # Ruta completa del archivo de origen y destino
    originRoute = os.path.join(sourceDirectory, file)
    destinationRoute = os.path.join(diretoryName, file)

    # Mover el archivo a la carpeta correspondiente
    shutil.copy(sourceDirectory, destinationDirectory)
    print(f"Copiando '{file}' a '{diretoryName}'")