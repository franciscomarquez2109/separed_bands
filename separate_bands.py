import os
import re
import shutil

# arreglo con las expresiones regulares
regularExpressions = [r'550nm',r'660nm',r'790nm',r'735nm']
# Directorio de origen donde se buscarán los archivos JPG

#ruta actual
CurrentRouter = os.getcwd()
sourceDirectory = CurrentRouter
# Directorio de destino donde se crearán las carpetas y se moverán los archivos
destinationDirectory = CurrentRouter + "/bandas"
print(destinationDirectory)

# Crear directorio de destino si no existe
if not os.path.exists(destinationDirectory):
    os.makedirs(destinationDirectory)

# Obtener la lista de archivos JPG en el directorio de origen
tifFiles = [tifFile for tifFile in os.listdir(sourceDirectory) if tifFile.lower().endswith('.tif')]

# Iterar sobre los archivos tif y moverlos a carpetas correspondientes
for tifFile in tifFiles:
    #Iterar sobre las expresiones regulares para buscar cada una de ellas en la lista de bandas
    for expression in regularExpressions:
        rowExpression = re.compile(expression)
         # Buscar la coincidencia con la expresión regular en el nombre del archivo
        coincidences = rowExpression.findall(tifFile)

        if len(coincidences) > 0:

            # asignamos el nombre de la banda que estamos buscando a la carpeta
            folderName = coincidences[0]

            # Crear directorio para el nombre si no existe
            directoryName = os.path.join(sourceDirectory, folderName)
            if not os.path.exists(directoryName):
                os.makedirs(directoryName)

            # Ruta completa del archivo de origen y destino
            originRoute = os.path.join(sourceDirectory, tifFile)
            destinationRoute = os.path.join(directoryName, tifFile)

            # copiar el archivo a la carpeta correspondiente
            shutil.copy(originRoute, destinationRoute)
            print(f"Copiando '{tifFile}' a '{directoryName}'")
            break

#obtenemos la lista de imagenes jpg para agregarlas a una carpeta en el mismo destino
jpgFiles = [jpgFile for jpgFile in os.listdir(sourceDirectory) if jpgFile.lower().endswith('.jpg')]

# nombre unico para la carpeta de imagenes
folderName = 'RGB'

 # Crear directorio para el nombre si no existe
directoryName = os.path.join(destinationDirectory, folderName)
if not os.path.exists(directoryName):
    os.makedirs(directoryName)

# Iterar sobre los archivos JPG y moverlos a carpetas correspondientes
for jpgFile in jpgFiles:
   
    # Ruta completa del archivo de origen y destino
    originRoute = os.path.join(sourceDirectory, jpgFile)
    destinationRoute = os.path.join(directoryName, jpgFile)

    # Mover el archivo a la carpeta correspondiente
    shutil.copy(originRoute, destinationRoute)
    print(f"Copiando '{jpgFile}' a '{directoryName}'")