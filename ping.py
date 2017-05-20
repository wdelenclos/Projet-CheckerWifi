from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
import os
import time
import httplib

red = (255, 0, 0)
green = (0, 255, 0)
hostname = "wdrenclos.fr"


starttime=time.time()

while True:
    c = httplib.HTTPConnection(hostname)
    c.request("HEAD", '')
    sense.load_image("hello.png")

    if c.getresponse().status == 200:
      sense.show_message("OK", text_colour=green)
      print hostname, ' actif !'
      sense.load_image("done.png")
    else:
      sense.show_message("HS", text_colour=red)
      print hostname, 'INACTIF'
      sense.load_image("erreur.png")

    print "Prochaine verification dans 60s  \n"
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))