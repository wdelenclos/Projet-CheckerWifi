from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
import os
import time
import httplib
import urlparse

red = (255, 0, 0)
green = (0, 255, 0)
url = "http://dev.wdelenclos.fr/"
wait = 120

starttime=time.time()

while True:
    sense.load_image("hello.png")
    o = urlparse.urlparse(url)
    conn = httplib.HTTPConnection(o.netloc)
    conn.request("GET",'')
    r1 = conn.getresponse()


    if r1.status == 200:
      sense.show_message("OK", text_colour=green)
      print url, ' actif !'
      sense.load_image("done.png")
    else:
      sense.show_message("HS", text_colour=red)
      print url, 'INACTIF'
      sense.load_image("erreur.png")

    print "Prochaine verification dans", wait , "s \n"
    time.sleep(wait)