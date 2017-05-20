#--- Requis
import sys
import os
import subprocess
import time
starttime=time.time()

print "\n\n\n############# Script d'actualisation des DNS de dev.wdelenclos.fr ###########"


while True:
  os.system('python cf-ddns.py')
  print "... prochaine verification dans 60s  \n "
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

print "\n\n\n############# Script fini ###########"