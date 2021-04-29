#-------------Modulos----------------#
#Audioplayer: reproduccion de sonidos
#Speech Recognition: reconocer la voz del usuario
#Settings: token que conecta con Wit Ai
#Wit: plataforma para reconcimiento de voz

from os import close
from audioplayer import AudioPlayer as ap
import speech_recognition as sr
import settings as token
from wit import Wit

#------------Constante parte historia------------#
#Evalua la parte de la historia donde nos encontramos
PARTE= 1
#----------------Rutas de audios------------------#
#Se almacenan las rutas de los audios que conforman la novela y se guardan en variables.  
parte_uno= "audio//parte_uno.wav"
parte_dos= "audio//parte_dos.wav"
parte_tres= "audio//parte_tres.wav"
parte_cuatro= "audio//parte_cuatro.wav"
parte_cinco= "audio//parte_cinco.wav"
parte_seis= "audio//parte_seis.wav"
parte_siete= "audio//parte_siete.wav"
parte_ocho= "audio//parte_ocho.wav"
parte_nueve= "audio//parte_nueve.wav"
parte_diez= "audio//parte_diez.wav"
parte_once= "audio//parte_once.wav"
parte_doce= "audio//parte_doce.wav"
parte_trece= "audio//parte_trece.wav"
parte_catorce= "audio//parte_catorce.wav"
parte_quince= "audio//parte_quince.wav"
parte_dieciseis= "audio//parte_dieciseis.wav"
parte_diecisiete= "audio//parte_diecisiete.wav"
parte_dieciocho= "audio//parte_dieciocho.wav"
parte_diecinueve= "audio//parte_diecinueve.wav"
parte_veinte= "audio//parte_veinte.wav"
parte_veintiuno= "audio//parte_veintiuno.wav"
parte_veintidos= "audio//parte_veintidos.wav"
parte_veintitres= "audio//parte_veintitres.wav"
parte_veinticuatro= "audio//parte_veinticuatro.wav"

#-----------------Activar microfono------------------#
#Se activa el microfono y obtiene lo que el usuario dijo para posteriormente pasarlo a Wit.ai y analizarlo. 
def micro_on():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla...")
        audio= r.listen(source)
        try:
            text= r.recognize_wit(audio, key=token.WIT_TOKEN)
            run(text)
        except:
            print("No te entendi. Repitelo...")
            micro_on()
            
#------------Recomendaciones iniciales--------------#
def inicio():
    ap(parte_uno).play(block=True)
    print("\nSugerencia: Lo deseo")
    micro_on()
    
#------------Analizando respuesta---------------#
#Se recibe el json de la respuesta del usuario y se analiza en Wit. Segun la respuesta se continua con la historia.
def run(text):
    client= Wit(token.WIT_TOKEN)
    resp= client.message(text)
    #print(resp)
    print('Analizando...')
    traits(resp)

def traits(response):
    print('Listo...')
    action= "Unknown"
    if 'traits' in response:
        pass
    if 'intents' in response:
        for x in response['intents']:
            if x['confidence'] > 0.8:
                if x['name'] == 'parte_uno':
                    return historia_parte_dos(response)
                elif x['name'] == 'parte_dos':
                    return historia_parte_tres(response)
                elif x['name'] == 'parte_tres':
                    return historia_parte_cuatro(response)
                elif x['name'] == 'parte_cuatro':
                    return historia_parte_cinco(response)
                elif x['name'] == 'parte_cinco':
                    return historia_parte_seis(response)
                elif x['name'] == 'parte_seis':
                    return historia_parte_siete(response)
                elif x['name'] == 'parte_siete':
                    return historia_parte_ocho(response)
                elif x['name'] == 'parte_ocho':
                    return historia_parte_nueve(response)
                elif x['name'] == 'parte_nueve':
                    return historia_parte_diez(response)
                elif x['name'] == 'parte_diez':
                    return historia_parte_once(response)
                elif x['name'] == 'parte_once':
                    return historia_parte_doce(response)
                elif x['name'] == 'parte_doce':
                    return historia_parte_trece(response)
                elif x['name'] == 'parte_trece':
                    return historia_parte_catorce(response)
                elif x['name'] == 'parte_catorce':
                    return historia_parte_quince(response)
                elif x['name'] == 'parte_quince':
                    return historia_parte_dieciseis(response)
                elif x['name'] == 'parte_dieciseis':
                    return historia_parte_diecisiete(response)
                elif x['name'] == 'parte_diecisiete':
                    return historia_parte_dieciocho(response)
                elif x['name'] == 'parte_dieciocho':
                    return historia_parte_diecinueve(response)
                elif x['name'] == 'parte_diecinueve':
                    return historia_parte_veinte(response)
                elif x['name'] == 'parte_veinte':
                    return historia_parte_veintiuno(response)
                elif x['name'] == 'parte_veintiuno':
                    return historia_parte_veintidos(response)
                elif x['name'] == 'parte_veintidos':
                    return historia_parte_veintitres(response)
                elif x['name'] == 'parte_veintitres':
                    return historia_parte_veinticuatro(response)
                else:
                    print("No es la respuesta que esperaba")
                    micro_on()
            elif x['confidence'] < 0.8:
                print("Repiteme eso ultimo...")
                micro_on()
            else:
                micro_on()
        else:
            micro_on()
    else:
        print("Pero que chorradas estas diciendo...")
        micro_on()

def historia_parte_dos(respuesta):
    if 'text' in respuesta:
        if 'deseo' in respuesta['text'] or 'quiénes son' in respuesta['text'] or 'quienes son' in respuesta['text']:
            ap(parte_dos).play(block=True)
            print("Sugerencia: La tormenta está muy fuerte.")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Repiteme lo que dijiste...")
        micro_on()

def historia_parte_tres(respuesta):
    if 'text' in respuesta:
        if 'tormenta' in respuesta['text']:
            ap(parte_tres).play(block=True)
            print("Sugerencia: ¿A donde iremos?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No te entendi nada, habla bien")
        micro_on()

def historia_parte_cuatro(respuesta):
    if 'text' in respuesta:
        if 'donde' in respuesta['text']:
            ap(parte_cuatro).play(block=True)
            print("Sugerencia: No dire nada")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Trata de vocalizar mejor y dilo de nuevo...")
        micro_on()
        
def historia_parte_cinco(respuesta):
    if 'text' in respuesta:
        if 'silencio' in respuesta['text'] or 'no' in respuesta['text'] and 'dire' in respuesta['text'] or 'ni' in respuesta['text'] or 'palabra' in respuesta['text'] or 'nada' in respuesta['text']:
            ap(parte_cinco).play(block=True)
            print("Sugerencia: Me encantaria ver eso")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("¿Eh?")
        micro_on()
        
def historia_parte_seis(respuesta):
    if 'text' in respuesta:
        if 'ver eso' in respuesta['text'] or 'me encantaria':
            ap(parte_seis).play(block=True)
            print("Sugerencia: Pero acabo de hablar")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No entiendo mandarin")
        micro_on()

def historia_parte_siete(respuesta):
    if 'text' in respuesta:
        if 'hablar' in respuesta['text']:
            ap(parte_siete).play(block=True)
            print("Sugerencia: Voy detras de ti")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Habla bien...")
        micro_on()

def historia_parte_ocho(respuesta):
    if 'text' in respuesta:
        if 'detras' in respuesta['text'] or 'voy' in respuesta['text'] or 'tras' in respuesta['text'] or 'detrás' in respuesta['text']:
            ap(parte_ocho).play(block=True)
            print("Sugerencia: El agua es tan cristalina")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No entendi...")
        micro_on()

def historia_parte_nueve(respuesta):
    if 'text' in respuesta:
        if 'agua' in respuesta['text'] or 'rio' in respuesta['text']:
            ap(parte_nueve).play(block=True)
            print("Sugerencia: Que raro, no tengo eco")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Creo que se te enredo la lengua")
        micro_on()

def historia_parte_diez(respuesta):
    if 'text' in respuesta:
        if 'eco' in respuesta['text']:
            ap(parte_diez).play(block=True)
            print("Sugerencia: ¿Que es este lugar?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Tienes que hacer ejercisios bocales")
        micro_on()

def historia_parte_once(respuesta):
    if 'text' in respuesta:
        if 'lugar' in respuesta['text']:
            ap(parte_once).play(block=True)
            print("Sugerencia: ¿Que llevan cargando?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No arrastres la voz")
        micro_on()

def historia_parte_doce(respuesta):
    if 'text' in respuesta:
        if 'llevan' in respuesta['text']:
            ap(parte_doce).play(block=True)
            print("Sugerencia: ¿Que son estos animales?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No entiendo tu dialecto")
        micro_on()

def historia_parte_trece(respuesta):
    if 'text' in respuesta:
        if 'que' in respuesta['text'] or 'son' in respuesta['text'] or 'estos' in respuesta['text']:
            ap(parte_trece).play(block=True)
            print("Sugerencia: ¿Hacia donde vamos?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No soy adivino, dilo de nuevo...")
        micro_on()

def historia_parte_catorce(respuesta):
    if 'text' in respuesta:
        if 'donde' in respuesta['text'] or 'vamos' in respuesta['text']:
            ap(parte_catorce).play(block=True)
            print("Sugerencia: No estaba preparado")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Repitelo...")
        micro_on()

def historia_parte_quince(respuesta):
    if 'text' in respuesta:
        if 'no' in respuesta['text'] or 'estaba' in respuesta['text'] or 'preparado' in respuesta['text']:
            ap(parte_quince).play(block=True)
            print("Sugerencia: ¿Quien es el?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Necesitas clases para hablar bien")
        micro_on()

def historia_parte_dieciseis(respuesta):
    if 'text' in respuesta:
        if 'quien' in respuesta['text'] or 'es' in respuesta['text'] or 'quién' in respuesta['text']:
            ap(parte_dieciseis).play(block=True)
            print("Sugerencia: ¿Y donde nos encontramos?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Mejora tu vocalizacion")
        micro_on()

def historia_parte_diecisiete(respuesta):
    if 'text' in respuesta:
        if 'donde' in respuesta['text'] or 'dónde' in respuesta['text'] or 'nos' in respuesta['text'] or 'encontramos' in respuesta['text'] or 'lugar' in respuesta['text']:
            ap(parte_diecisiete).play(block=True)
            print("Sugerencia: Hay criaturas en el techo")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("No arrastres la voz")
        micro_on()

def historia_parte_dieciocho(respuesta):
    if 'text' in respuesta:
        if 'criaturas' in respuesta['text'] or 'animales' in respuesta['text'] or 'techo' in respuesta['text'] or 'arriba' in respuesta['text']:
            ap(parte_dieciocho).play(block=True)
            print("Sugerencia: Se escucha el mar")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Otra vez...")
        micro_on()

def historia_parte_diecinueve(respuesta):
    if 'text' in respuesta:
        if 'escucha' in respuesta['text'] or 'oye' in respuesta['text'] or 'mar' in respuesta['text'] or 'oceano' in respuesta['text']:
            ap(parte_diecinueve).play(block=True)
            print("Sugerencia: ¿Y ahora donde estamos?")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("¿Que, que, que?")
        micro_on()

def historia_parte_veinte(respuesta):
    if 'text' in respuesta:
        if 'ahora' in respuesta['text'] or 'donde' in respuesta['text'] or 'dónde' in respuesta['text']:
            ap(parte_veinte).play(block=True)
            print("Sugerencia: Me da panico montar")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("¿Que idioma estas usando ahora?, dilo de nuevo")
        micro_on()

def historia_parte_veintiuno(respuesta):
    if 'text' in respuesta:
        if 'montar' in respuesta['text'] or 'panico' in respuesta['text'] or 'miedo' in respuesta['text'] or 'pánico' in respuesta['text']:
            ap(parte_veintiuno).play(block=True)
            print("Sugerencia: Ha sido grandioso")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Apenas y comprendi")
        micro_on()

def historia_parte_veintidos(respuesta):
    if 'text' in respuesta:
        if 'grandioso' in respuesta['text'] or 'fantastico' in respuesta['text'] or 'increible' in respuesta['text']:
            ap(parte_veintidos).play(block=True)
            print("Sugerencia: Ve tu delante, yo te sigo")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Trata de decirlo mas fuerte")
        micro_on()

def historia_parte_veintitres(respuesta):
    if 'text' in respuesta:
        if 'delante' in respuesta['text'] or 'sigo' in respuesta['text']:
            ap(parte_veintitres).play(block=True)
            print("Sugerencia: Lo escuchare siempre")
            micro_on()
        else:
            print("¿Eh?")
            micro_on()
    else:
        print("Habla con mas claridad")
        micro_on()

def historia_parte_veinticuatro(respuesta):
    ap(parte_veinticuatro).play(block=True)
    