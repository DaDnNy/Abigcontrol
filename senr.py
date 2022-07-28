from time import sleep
import utime
from hcsr04 import HCSR04
from machine import Pin, PWM
from machine import Timer
import network, time
from machine import Pin, I2C, ADC  # Importamos el módulo machine
import time  #Importamos el módulo de tiempo time https://docs.python.org/es/3/library/time.html
import urequests

buzzer= Pin(19, Pin.OUT) #asig al objeto buzzer el pin #19 

medidor = HCSR04 (trigger_pin = 5, echo_pin = 18) #asignacion de sensor al atributo medidor

pir = Pin(35, Pin.IN, Pin.PULL_DOWN)# pulsador conectado a 3.3 vol indentificacion del senspor pir1 y asignacion al pin 35 en la esp32
pir1=Pin(33, Pin.IN, Pin.PULL_DOWN) #indentificacion del senspor pir1 y asignacion al pin 33 en la esp32              

ledn= Pin(32,Pin.OUT) #led asignado a pir en el pin 32 de esp32
ledA= Pin(25,Pin.OUT)#ledA asignado a pir en el pin 25 de esp32
ledR= Pin(26,Pin.OUT)
led1= Pin(2,Pin.OUT)
led2= Pin(4,Pin.OUT)
def conectaWifi (self, red, password):
    miRed = network.WLAN(network.STA_IF)
    print('Entro')

class Movimiento():
    def __init__(self):
        self.alerta=0 #atributo global
        
    def conectaWifi (self, red, password): #funcion para la conexion a la red se realiza llamado en el main
        miRed = network.WLAN(network.STA_IF)
        print('Entro')
        if not miRed.isconnected():
            miRed.active(True)                   #activa la interface
            miRed.connect(red, password)         #Intenta conectar con la red
            print('Conectando a la red', red +"…")
            timeout = time.time ()
            while not miRed.isconnected(): #Mientras no se conecte..
                if (time.ticks_diff (time.time (), timeout) > 10):
                    return False
            return True
        
    def telegram_bot_sendtext(self,bot_message):# funcion de creacion del BOT de Telegram
        self.msm=bot_message
        bot_token = '5529503668:AAE8SC6WLBn3Ts8an3JbrAPHaS_D-eHBM9U' #asigma la Id de Telegram al atrubuto Bot_Token
        bot_chatID = '1729745969' # asigna a Chat ID la Id de conexion a Telegram
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + self.msm
        response = urequests.get(send_text)
        #print("Movimientos detectados")
        return response.json()

    def sensorM(self): #metodo de Sensores de Movimiento y  sensor Ultrasonido         
        while True:
            distancia = medidor.distance_cm () #le asicna la atributo distacia la distacia en Cm del sensor Ultrasonido
            estado = pir.value() # se le asigna a atrib Estado el valor de Pir(sensores de movimiento)
            estado2= pir1.value()# se le asigna a atrib Estado2 el valor de Pir2 (sensores de movimiento)
            utime.sleep_ms(1)
            
            if estado==1 and estado2==0: #Valida si EL VALOR DE ESTADO ES 1 o on 
                print("hay detencion de movimiento en la zona 1")
                #test = telegram_bot_sendtext('hay detencion de movimiento en la zona 1')
                ledn.on() # enciende el Led si el Valor es verdadero
                ledA.off()
                ledR.off()
                utime.sleep_ms(1)
            if estado==0 and estado2==1:#Valida si EL VALOR DE ESTADO2 ES 1 o on 
                print("hay detencion de movimiento en la zona 2")
                ledA.on() #enciende el ledA si el valor de estado2 es verdadero
                ledn.off()
                ledR.off()
                utime.sleep_ms(1)# tiempo de realizacion de la accion
            if estado2==1 and estado==1: #Valida si los dos estados son verdaderos
                print("hay movimiento en la zona 1 y 2")#Muestra un mensaje de alerta
                ledR.on() #enciende otro led si los dos estados son verdaderos
                ledn.off()
                ledA.off()          
                utime.sleep_ms(1)
            if (distancia>=0 and distancia<=90): #si el sensor HCSR04 detecta movimientos a distacia de 0 a 90cm 
                buzzer.value(1) #si detecta movimientos a una distacia menor o igual a los 90 se enciende el buzzer
                led1.value(0) #led apagado
                led2.value(0)#led apagado
                print("se detecta intrusión a: ", distancia," cm") #imprime lo que detecta en el atributo distacia
                sleep (1) #en tiempo
            if(distancia>=91 and distancia<=279):
                led1.value(1)
                buzzer.value(0)
                led2.value(0)
                print("se acerca alguien a la Zona: ",distancia," cm")
                sleep(1)
            if(distancia>=380 and distancia<=400):
                
                led2.value(1)
                buzzer.value(0)
                led1.value(0)
                print("se detecta movimiento a una distacia de: ",distancia," cm")
                #test = telegram_bot_sendtext('se detecta movimiento a una distacia de:',distancia)
                sleep(1)
            else:                                                    
                    #print("No se detecta movimiento en ninguna zona")
                ledn.off()
                ledA.off()
                ledR.off()
                led1.value(0)
                led2.value(0)
                buzzer.value(0)
                utime.sleep_ms(1)
            