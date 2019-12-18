
from machine import Pin
from neopixel import NeoPixel
import time

n = 7
pin = Pin(5, Pin.OUT)   # set GPIO5 (D1) to output to drive NeoPixels
np = NeoPixel(pin, 7)   # create NeoPixel driver on GPIO0 for 7 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
np[0] = (0, 0, 0) # set the first pixel to nothing (black)
np.write()              # write data to all pixels

def cycle():
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

def bounce():
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

def fade():
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
