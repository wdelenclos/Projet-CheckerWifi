
#--- Requis
from sense_hat import SenseHat
import sys
import os
import subprocess


# --- Demarrage
sense = SenseHat()



p = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('hostapd' in out):
    sense.load_image("wifi.png")
else:
     sense.load_image("close.png")
