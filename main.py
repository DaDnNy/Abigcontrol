from senr import Movimiento
import network, time
#from hcsr04 import HCSR04
#from time import sleep
import utime
from machine import Pin,Timer
wf = Movimiento()
msm = Movimiento()
ledA= Pin(25,Pin.OUT)#
if wf.conectaWifi("FAMILIA LOPEZ", "Ti852456"):#se conecta a la red 
   print ("Conexión exitosa!")
    
else:
   print ("Imposible conectar")
#while True: # envio de alertas a Telegram

msm.telegram_bot_sendtext('Se detecto movimiento en el sensor en la Zona2')
                                             
sm = Movimiento()
sm.sensorM()
