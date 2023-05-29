#!/usr/bin/python3

import RPi.GPIO as gpio
import smbus
from ADS1x15 import ADS1115
import time
import matplotlib.pyplot as plt
import os
import sys
import numpy as np

# Sensor
adc = ADS1115()
channel = 0
gain = 1
data = 0

# Algorytm
m_light = True


# GPIO
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(19, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(35, gpio.OUT)

# parameter for corss correlation
scope =100
d =0
l =[]
l_init=[]
erg = 0
erg_2 = 0
l_max = 0
l_two = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.161, 0.247, 0.398, 0.52, 0.633, 0.743, 0.819, 0.895, 0.921, 0.95, 1, 1, 0.97, 0.94, 0.9, 0.85, 0.824, 0.821, 0, 0, 0, 0, 0, 0, 0, 0, 0.681, 0.772, 0.854, 0.91, 0.965, 1.0, 0.951, 0.953, 0.935, 0.87, 0.841, 0.805, 0.744, 0.741, 0.71, 0.748, 0.676, 0.605, 0.536, 0.495, 0.453, 0.426, 0.417, 0.387, 0.353, 0.296, 0.237, 0.193, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Initialisation empy field for measurement data
for i in range(scope):
    l_init.append(0)
l = [*l_init]


try:
    while True:
        # read sensor Data (loudness sensor)
        data = adc.read_adc(channel, gain)
        l.pop(0)
        l.append((data-5000)*(-1))

        # if data point 15 is over the threshold of 1000, the cross coreation starts
        if l[15]>(1000):
            # typisierung
            l_max = max(l)
            for idx, i in enumerate(l):
                l[idx]= np.around((i/l_max), 3)
            # corss correlation
            erg = np.sum(np.multiply(l,l_two ))
            print(l)
            print("2:", erg)
            # erg > 14: result of corss correlation is true
            if erg > 14:
                print("two times clapping detected")
                # turn on or off the light, depend on the saved state
                if m_light:
                    os.system("/./home/pi/433Utils/RPi_utils/codesend 1377617 24")
                    m_light = False
                else:
                    os.system("/./home/pi/433Utils/RPi_utils/codesend 1377620 24")
                    m_light = True
                plt.plot(l)
                plt.plot(l_two )
                break

            # erg < 14: result of corss correlation is false. No  right clapping detected
            l = [*l_init]

            time.sleep(0.2)

        # if file is create, abort while loop and stop the script
        if os.path.isfile("/var/www/html/stop_script"):
            break

finally:
    pass


plt.axis([0,scope,-1,1])
plt.grid(True)
plt.show()

