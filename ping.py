from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
import os
import time

red = (255, 0, 0)
green = (0, 255, 0)
hostname = "dev.wdetttgthhtlenclos.fr"
starttime=time.time()

while True:
    response = os.system("ping -c 1 " + hostname)
    sense.load_image("hello.png")
    time.sleep(2)
    if response == 0:
      sense.show_message("OK", text_colour=green)
      print hostname, ' actif !'
      sense.load_image("done.png")
    else:
      sense.show_message("HS", text_colour=red)
      print hostname, 'INACTIF'
      sense.load_image("erreur.png")

    print "Prochaine verification dans 60s  \n"
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))