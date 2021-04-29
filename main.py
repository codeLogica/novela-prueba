from os import close
from time import sleep
import app

archivo= open('main.py')

#----------------Instrucciones-------------------------#
instrucciones= "\n         ¡Bienvenidos a esta aventura!       \nHemos tratado de que se convierta en una historia \nampliamente inmersiva por lo que para continuar hay \nuna serie de recomendaciones a seguir:\n\n1. Uso de auriculares obligatorio\n2. Seguir instrucciones que aparezcan en pantalla\n3. Usa tu propia voz y habla al indicarse (seguir sugerencia)\n6. Espera la indicacion para volver a hablar\n5. Divertirse\n\nDado que esto es una audio historia interactiva\nempezemos con el audio..."

lista_char= []

for char in instrucciones:
    sleep(0.1)
    print(char, end="", flush=True)

app.inicio()

archivo.close()

