from machine import Signal, Pin, ADC
from time import sleep
from lights import *

ledPin2 = machine.Pin(2, machine.Pin.OUT)
Led2 = Signal(ledPin2, invert=True)

adc = ADC(0)

val = 0
lastledOn = False
ledOn = False

while True:
  val = adc.read()
  print(val)
  if val < 50:
    ledOn = True
  else:
    ledOn = False
  sleep(0.25)
  print(ledOn)
  sleep(0.25)
  #print(lastledOn)
  if ledOn != lastledOn:
    if ledOn == True:
      bounce()
      print("bounce!")
    else:
      cycle()
      sleep(0.5)
      print("cycle!")
      sleep(0.5)
    ledOn = lastledOn
