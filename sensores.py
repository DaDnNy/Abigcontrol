from hcsr04 import HCSR04
from time import sleep
import utime
from machine import Pin

medidor = HCSR04 (trigger_pin = 13, echo_pin = 12)
#_________

ledAzul= Pin(15,Pin.OUT)
ledAmarillo= Pin(2,Pin.OUT)
ledRojo= Pin(4,Pin.OUT)

class sensorAll():
    def __init__ (self):
        pass
    def sensorD(self):
        while (True):
            try:
                distancia = float(medidor.distance_cm ())
        #print ("La distancia en este momento es:  ", distancia, "cm")
                if distancia >= 190:
                    ledAzul.value(1)
                    sleep (1)
                    print("en este momento no hay movimiento", distancia, "cm")
            
                elif distancia >= 100 and distancia<=189:
                    ledAmarillo.value(1)
                    sleep (1)
                    print("Se acerca alguien", distancia, "cm")
            
                elif distancia >= 0 and distancia <100:
                    ledRojo.value(1)
                    sleep (1)
                    print("Ojo hay movimiento en la zona", distancia, "cm")
            
                else:
                    ledAzul.value(0)
                    ledAmarillo.value(0)
                    ledRojo.value(0)
                    print("No hay nadie")
                    sleep (1)
            except:
                print ("Error!")
                
                
        def sensorM(self):
            
            pir = Pin(19, Pin.IN, Pin.PULL_DOWN)# pulsador conectado a 3.3 vol
            pir1=Pin(21, Pin.IN, Pin.PULL_DOWN)
            
            led= Pin(5,Pin.OUT)
            ledA= Pin(18,Pin.OUT)
            
            while True:
                estado = pir.value()
                estado2= pir1.value()
                utime.sleep_ms(1)
                if estado==1 and estado2==0:
                    print("hay detencion de movimiento en la zona 1")
                    led.on()
                    ledA.off()
                    utime.sleep_ms(1000)
                elif estado==0 and estado2==1:
                    print("hay detencion de movimiento en la zona 2")
                    led.on()
                    ledA.off()
                    utime.sleep_ms(1000)
                elif estado2==1 and estado==1:
                    print("hay movimiento en la zona 1 y 2")
                    led.on()
                else:
                    print("No se detecta movimiento en ninguna zona")
                    led.off()
                    ledA.off()
                    
        '''def sensorIf (self):
            
            Infrarojo = Pin(34, Pin.IN, Pin.PULL_DOWN)# pulsador conectado a 3.3 vol
            
            buzzer = Pin (35,Pin.OUT)
         
            
            while True:
                estado = Infrarojo.value()
                
                utime.sleep_ms(1)
                if estado==1:
                    print("se a detectado alguien")
                    buzzer.on()
                    
                    utime.sleep_ms(1000)
                else:
                    print("No se detecta movimiento en ninguna zona")
                    buzzer.off()'''
  