#ED 2021-01
from gpiozero import LED

i = 1

import os
import time

#for j in range(10):
while True:
  os.system('echo 1 | dd status=none of=/sys/class/leds/led0/brightness') # led on
  time.sleep(1)
  os.system('echo 0 | dd status=none of=/sys/class/leds/led0/brightness') # led off
  time.sleep(1)


