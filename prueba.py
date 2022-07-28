import network, time
import urequests

def conectaWifi (red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
         miRed.active(True)                   #activa la interface
         miRed.connect(red, password)         #Intenta conectar con la red
         print('Conectando a la red', red +"…")
         timeout = time.time ()
         while not miRed.isconnected():           #Mientras no se conecte..
             if (time.ticks_diff (time.time (), timeout) > 10):
                 return False
     return True

if conectaWifi ("FAMILIA LOPEZ", "Ti852456"):

   print ("Conexión exitosa!")
   print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())       
else:
    print ("Imposible conectar")
    miRed.active (False)

def telegram_bot_sendtext(bot_message):

    bot_token = '5529503668:AAE8SC6WLBn3Ts8an3JbrAPHaS_D-eHBM9U'
    bot_chatID = '1729745969'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = urequests.get(send_text)

    return response.json()

test = telegram_bot_sendtext('se a detectado movimiento en le sensor')