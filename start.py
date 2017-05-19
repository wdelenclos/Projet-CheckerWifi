#--- Requis
from sense_hat import SenseHat
import sys
import os
import subprocess
import time
starttime=time.time()

# --- Demarrage
sense = SenseHat()

print "\n\n\n############# Bonjour Wladimir ###########"

while True:
  os.system('python script.py')
  sense.load_image("wifi.png")
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

