# Script de clasificación de bandas espectrales de archivos tif

## Descripción
Esta aplicación procesa archivos TIFF y JPG, organizándolos en carpetas según las bandas espectrales especificadas. Los archivos TIFF que contienen nombres que coinciden con expresiones regulares predefinidas se mueven a carpetas correspondientes. Además, los archivos JPG se agrupan en una carpeta especial llamada 'RGB'.

## Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/franciscomarquez2109/separed_bands.git
2. Copia el archivo "separate_bands.py" a la ruta de los archivos que deseas clasificar:
    ```bash
    cp separate_bands.py ruta_destino
3. Ejecute el archivo:
    ```bash
    python separate_bands.py