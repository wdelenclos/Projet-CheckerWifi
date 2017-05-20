#--- Requis
import sys
import os
import subprocess
import time
starttime=time.time()

# --- Demarrage
sense = SenseHat()

print "\n\n\n############# Script d'actualisation des DNS de dev.wdelenclos.fr ###########"
i = 0

while True:
  os.system('python cf-ddns.py')
  i++
  print "Verification " + i + " faite"
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

print "\n\n\n############# Script fini ###########"