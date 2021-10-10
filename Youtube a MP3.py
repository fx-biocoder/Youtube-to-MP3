#   1 - Librerías necesarias para el proyecto
from pytube import YouTube # IMPORTANTE! Actualizar pytube ($ python -m pip install --upgrade pytube)
import re, easygui as eg

#   2 - Ventana que solicita el enlace de Youtube
enlace = eg.enterbox("Introduzca el enlace de Youtube a convertir", "Youtube a MP3")

#   3 - Validación del enlace y descarga
#       La validación se realiza mediante expresiones regulares y luego se procede a la descarga
#       Si la validación falla el programa se cierra y debe abrirse nuevamente
if(re.search("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$", enlace)):
    try:
        video = YouTube(enlace)
        audio = video.streams.filter(only_audio=True, file_extension = "mp4").first()   #   Descarga únicamente el audio del primer stream que se encuentra en formato .mp4
        audio.download(output_path = eg.filesavebox(default = "Audio - Youtube a MP3", filetypes = ".mp3"))
        print("La descarga se ha realizado exitosamente")
    except:
        print("La descarga no pudo realizarse. Intente actualizar pytube (python3 -m pip install --upgrade pytube)")
else:
    print("El enlace no es válido, por favor intente nuevamente utilizando un enlace de Youtube")