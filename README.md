## Wearable Technology Badge Workshop

<img src="https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F85203521%2F19213558993%2F1%2Foriginal.20191220-122025?w=800&auto=format%2Ccompress&q=75&sharp=10&rect=14%2C0%2C610%2C305&s=6e27e184fdfa4b9a972081742b81bc35" width="600">

Make a small interactive rechargeable wearable badge over 4 weeks to get you started in the world of wearable technology. Designed to give you an understanding of basic fundamentals in electronics, embroidery and coding in the versatile progamming language micropython to control interactive intimate wearables.  We'll use DIY conductive yarn pressure sensors and variants of low cost ESP8266 development boards that can help you deploy all kinds of wearable (and non-wearable) technology.

With this experience you'll be able to prototype and deply wearable tech for art, performance, fashion, product development. It's a chance to share your ideas with peers and meet other members of the DoES Liverpool community and get to know our facilities for the future.

All materials are provided, with extensive workshop notes, reference and resources here plus your own kit featuring an ESP8266 development board, Sublimation printed sensor, single and 6-ring NeoPixels, and a rechargeable battery pack you can for your next project.

Under 16s must be accompanied by a parent or guardian, suitable for ages 12 and up.

### Structure

 1. [Analog Textile Sensor making](#session-1)
 1. [LED & NeoPixel control with ESP8266 and MicroPython](#session-2)
 1. [Analog Sensor & ESP8266](#session-3)
 1. [Advanced ESP8266, sensor & LED control & Wearable Badge constructing](#session-4)

### Session 1

Make & test an analog textile sensor to understand the basics of electrical resistance and the flow of current in a simple circuit.

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electronics-green.svg?longCache=true&style=plastic)


<img src="images/session1/Session_1_Circuit_Image.png" width="400">

Our breadboard lets us easily connect electronic components and wire of the correct gauge clearly without the components falling out. They are how people prototype a circuit, and quite often you will rewire it in a way that's more robust and permanent or even design and make your own printed circuit boards (PCBs). On these mini 170-point breadboards there are 2 columns of 17 rows of 5 pins. Each 5 pin set on a  row are connected electrically so current flows through components. We generally dont use voltage over 12V when using these breadboards so we never have anything close to mains voltage. We are not even going above 3.7V with our wearables!

Follow the pictures below to make the circuit and compare it with the circuit diagrams provided. That's how you'll find diagrams on the internet and in electronics books, so it's worth having a look at those and doing some further research.

#### Circuit

<img src="images/session1/1/1.jpg" width="400">

Insert your LED. It matters which way the LED goes in; it's got a negative cathode `-` and a positive anode `+` if you get it wrong you can damage it. The long leg of the LED is `+'ve`, the shorter leg, the cathode, is `-'ve'`

<img src="images/session1/1/2.jpg" width="400">

Add your coin cell holder and coin cell. Be careful you understand the `+'ve` and `-'ve` cathod and anode. The `+` on the coin cell should be visible facing up, the Flat side of the coin cell holder is `-`

<img src="images/session1/1/3.jpg" width="400">

Add a red jumper wire connecting the long leg `+` anode of the LED with the `+` anode of the coin cell holder, the pin nearest the flat side of the holder

<img src="images/session1/1/4.jpg" width="400">

Add a 100 Ohm resistor

<img src="images/session1/2/8.jpg" width="400">

Connect your completed Fabric sensor.

<img src="https://user-images.githubusercontent.com/8654515/72371763-efbcae80-36fc-11ea-8d14-13dd224ededc.jpg" width="400">
Stitch onto the felt with the resistive thread, leaving a long piece on the back of the felt before your first stitch

<img src="https://user-images.githubusercontent.com/8654515/72371771-f0eddb80-36fc-11ea-990e-8f0d262bd25a.jpg" width="400">


<img src="https://user-images.githubusercontent.com/8654515/72371783-f5b28f80-36fc-11ea-9aa2-93fa34d648ef.jpg" width="400">
Make some stitches close together some can be touching but not overlapping or on top of one another

<img src="https://user-images.githubusercontent.com/8654515/72371789-f8ad8000-36fc-11ea-8e0a-334231272d38.jpg" width="400">
Continue until you have stitched along the back of the design, its fine to leave gaps. Leave a piece trailing at the other end.

<img src="https://user-images.githubusercontent.com/8654515/72371791-f9dead00-36fc-11ea-9184-d17322443f5c.jpg" width="400">


<img src="https://user-images.githubusercontent.com/8654515/72371792-fba87080-36fc-11ea-88c5-f606972d1abc.jpg" width="400">
Tie a piece of conductive thread to one end of the stitching
Stitch and add a snap fastener, then repeat at the other side with conductive thread.

<img src="https://user-images.githubusercontent.com/8654515/72371794-fcd99d80-36fc-11ea-9517-2dbd8afebe98.jpg" width="400">
Solder wires onto the other side of the snap fasteners.

<img src="https://user-images.githubusercontent.com/8654515/72371797-fea36100-36fc-11ea-9f42-789dc24dbb6a.jpg" width="400">
Clip the fasteners together


#### Component List

Component|No.|Source|Produced|Notes
--|--|--|--|--
170 point<br>mini breadboard|1|DoES|China|For prototyping
3V CR2032 coin cell battery|1|Ebay|
Two Pin Button|1|[Taydae Electronics](https://www.taydaelectronics.com/tact-switch-6-6mm-5mm-through-hole-spst-no.html)|China|simple breadboard compatible button
CR2032-compatible Watch Battery holder|1|[BatteryHolders.com](http://batteryholders.com/part.php?pn=BC2032-E2&original=CR2032&override=CR2032)|China|Easy breadboarding holder
Red Stripped solid core 22AWG wire|1|[Farnell](https://uk.farnell.com/c/cable-wire-cable-assemblies/hook-up-wire?wire-gauge=22awg)|[Alphawire](http://www.alphawire.com/) New Jersey US|Stripped fits into breadboards easily
Green Stripped solid core 22AWG wire|1|[Farnell](https://uk.farnell.com/c/cable-wire-cable-assemblies/hook-up-wire?wire-gauge=22awg)|[Alphawire](http://www.alphawire.com/) New Jersey US|Stripped fits into breadboards easily
Resistor 100 Ohm|1|Ebay|China|Resistor; fits anyway round (polarity doesn't matter)
Resistor 10K Ohm|1|Ebay|China|Resistor; fits anyway round (polarity doesn't matter)

This first step develops the basics of a pressure sensor; we can refer to more complex and accurate sensors and reflect on their usage.

### Further Reading

You can read about an alternative form of pressure sensor using [Velostat](https://www.adafruit.com/product/1361) that Laura made for another workshop using a similar microcontroller [Microbit](https://www.microbit.org/) belwo, that also runs micropython the programming language we are using to control our sensors and LED's.

[Pressure sensor build](https://github.com/DoESLiverpool/what-does-health-look-like/tree/master/pressure-sensor)

### Session 2

![Skill Covered](https://img.shields.io/badge/skill-python-black.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-screen-blue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-terminals-lightblue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-esp8266-gold.svg?longCache=true&style=plastic)

Flash LEDs using micropython on the ESP8266


#### Micropython and the ESP8266

<img src="images/ESP8266-Dev-Board-pinout.jpg" width="600">

The ESP8266 and it's larger ESP32 cousin is a powerful self contained microcontroller breakout board that is like arduino except incredibly powerful flexible and cheap, it's able to run web browsers, control LED's and motors and respond to a range of analog and digital sensors. What's special is that it can run micropython a powerful high level programming language which means that is quite easy to use and write even without being a programmer.

We're using the a few variant breakout boards of the ESP8266 like the WeMos D1 Mini Development Board in the diagram above or the bigger [ESP-12E-CP2102](https://www.ebay.co.uk/itm/Esp8266-Esp-12E-Cp2102-Wifi-Network-Development-Board-Module-For-Node-Mcu-GD/264530529453) variant which you can see above with its `GPIO` pin arrangement. We'll be using these in our workshops and you'll be able to take them home.

Don't worry about the seemingly contradictory annotations on the diagram, it will make sense. We are first of all only using the 'pin' (the metal legs that fit a breadboard)

You can refer to the [MicroPython tutorial for ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/index.html#micropython-tutorial-for-esp8266) for full details, but we've selected.

#### Connecting up

<img src="https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/esp8266-cp2102-driver.jpg?w=750&ssl=1" width="600">

You will need `CP2102` USB Module drivers to work with our ESP8266's which are the `CP2102` variants which you can get from [Silicon Labs](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers). We've also archived the windows & macos drivers in the workshop repo [here](drivers/CP2102)

Linux distributions often include CP2102 drivers built in, although Linux user accounts may need membership of the 'dialout' or 'serial' permission groups to access the device.

We use these drivers so we can access our ESP8266 boards over their serial port over USB.

### Software

There are a few ways to send commands and files to the ESP8266. We are using some new software we've found, [uPyCraft](https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/) which is easier for beginners. It let's you send commands and talk to the board line by line, and save complete files to the board that run when you are ready to deploy your project and run off batteries.

There's some more advanced alternatives using the [command line below](#command-line-alternatives-to-upycraft)

### Setting up uPyCraft

More To Follow.

If you follow the links on the random nerd tutorials it seems to imply that you must install python on your machine first. You don't need to do this!

[Windows](https://randomnerdtutorials.com/uPyCraftWindows)
[Mac](https://randomnerdtutorials.com/uPyCraftMac) (Ensure you allow apps to be downloaded from anywhere in your system security settings
[Linux](https://randomnerdtutorials.com/uPyCraftLinux)

### Sending the micropython firmware to the board

You need to send the micropython software to the board first. [Download it here](micropython) and note it's location. You need to click on the `.bin` file and then you will get a download box option on the webpage.

#### Selecting Serial Port

Go to **Tools** \> **Serial** and select your ESP8266 COM port (in our case it's COM5).

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/uPyCraft-IDE-Select-Serial-Port-COM5.png?resize=692%2C576&ssl=1)

[**Important:**]{style="color: #ff0000;"} if you plug your ESP8266 board to your computer, but you can't find the ESP8266 Port available in your uPyCraft IDE, it might be one of these two problems: **1.** USB drivers missing or **2.** USB cable without data wires.

**1.** If you don't see your ESP's COM port available, this often means you don't have the USB drivers installed. Take a closer look at the chip next to the voltage regulator on board and check its name.

The [ESP8266 ESP-12E NodeMCU](https://makeradvisor.com/tools/esp8266-esp-12e-nodemcu-wi-fi-development-board/) board uses the **CP2102** chip.

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/esp8266-cp2102-driver.jpg?resize=750%2C388&ssl=1)

After they are installed, restart the uPyCraft IDE and you should see the COM port in the **Tools** menu.

**2.** If you have the drivers installed, but you can't see your device, double-check that you're using a USB cable with data wires.

USB cables from powerbanks often don't have data wires (they are charge only). So, your computer will never establish a serial communication with your ESP8266. Using a a proper USB cable should solve your problem.

#### Selecting the Board

Go to **Tools** \> **Board**. For this tutorial, we assume that you're using the ESP8266, so make sure you select the "**esp8266**" option:

![](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/uPyCraft-IDE-Select-Board-ESP8266.png?resize=692%2C576&ssl=1)

### Flashing/Uploading MicroPython Firmware

Finally, go to **Tools** \> **BurnFirmware** menu to flash your ESP32 with MicroPython.

![](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/uPyCraft-IDE-Tools-burn-Firmware.png?resize=693%2C576&ssl=1)

Select all these options to flash the ESP8266 board:

-   board: **esp8266**
-   burn\_addr: **0x0**
-   erase\_flash: **yes**
-   com: **COMX** (in our case it's COM5)
-   Firmware: Select `Users` and choose the `ESP8266 .bin`
file you downloaded earlier

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/flash-firmware-esp8266-prepare.png?resize=692%2C576&ssl=1)

After pressing the "**Choose**" button, navigate to your Downloads
folder and select the ESP8266 *.bin* file:

![](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/select-esp8266-bin-file-uPyCraft-IDE.png?resize=813.75%2C490&ssl=1)

Having all the settings selected, hold-down the "**BOOT/FLASH**" button in your ESP8266 board:

![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/esp8266-flash-button.jpg?resize=547%2C385&ssl=1)

While holding down the "**BOOT/FLASH**", click the "**ok**" button in the burn firmware window:

![](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/OK-flash-firmware-esp8266.png?resize=452%2C282&ssl=1)

When the "**EraseFlash**" process begins, you can release the "**BOOT/FLASH**" button. After a few seconds, the firmware will be
flashed into your ESP8266 board.

![](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/esp8266-firmware-flashing-message.png?resize=602%2C182&ssl=1)

**Note:** if the "**EraseFlash**" bar doesn't move and you see an error message saying "**erase false.**", it means that your ESP8266 wasn't in flashing mode. You need to repeat all the steps described earlier and hold the "**BOOT/FLASH**" button again to ensure that your ESP8266 goes into flashing mode.

<img width="400" src="https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/10/micropython-erase-false-message-failed.png?resize=143%2C120&ssl=1">


You should see the python prompt in the bottom console window

```
>>>
```

### Micropython Command Walkthrough

We generally prototype code by running it line by line, a bit like having a conversation with your board. We like the way that weirdly makes you feel more connected to it and we think it might help you learn. After that we can make and send python files to run independently of our computers.

The bottom window of uPyCraft is the console. This gives you messages telling you if you've downloaded things correctly, any issues with the board so you know whats going on.

<img src="images/session2/uPyCraftConnectIcon.png" width="150">

Once you connect to the board using the connect icon above you'll see the python prompt


```
>>>
```
You can now 'talk' to the board. Start with typing

`print("hello")` You should get a reply hello on the next line!

### Controlling the onboard blue LED

In python we `import` the tools inside micropython that we need to do what we want.

Get the machine module to control our ins and outs

`import machine`

Lets define a Pin as an output, using the onboard LED which is called Pin no. 2

`ledPin2 = machine.Pin(2, machine.Pin.OUT)`

This should turn the LED on!

Now try:

`ledPin2.off()`

Annoyingly defining the pin like this means off has no effect, but we can use Signal to abstract away this.

`from machine import Signal`

`Led2 = Signal(ledPin2, invert=True)`

now things will work more intuitively if we use Led2 instead!

`Led2.off()`
`Led2.on()`


### NeoPixels

To wire up you just connect `3.3V`(marked as `3V3` on your board) to `+VCC` on the neopixel, `GND` (marked `GND` on your board) to `GND` on the neopixel, and `GPIO5` (marked as `D1` on your board to the `IN` or `DIN` on the neopixel. NeoPixels have got all the resistors on board so you wont need to protect your Digital pins when using them.


NeoPixels are addressable RGB LEDs and micropython has a library module just for that! Add the [`lights.py`](https://github.com/cheapjack/WearableTechBadge/blob/master/examples/circle/lights.py) script to your board and with a quick

### Single NeoPixel Use

I'll update this by the end of the week so you can play at home.

```
from lights import *
```
### Making Permanent Changes

So far we've just been sending messages over the serial console in the bottom window of the uPyCraft IDE.

For our micropython code to work after we've disconnedted you need to make a `main.py` file on the board. To do this once connected to your ESP8266 you need to write your code in a folder called  into the folder called `device` on the top right of `uPyCraft`

Make a new file with the icon above. If asked call it `main.py`

Copy and paste the below into it and save it.

```
from machine import Signal, Pin
from time import sleep

ledPin2 = machine.Pin(2, machine.Pin.OUT)
led2 = Signal(ledPin2, invert=True)
led2.off()

while True:
    led2.on()
    sleep(0.5)
    led2.off()
    sleep(0.25)
```

You should be already connected to the board. Click the big arrow icon on the right to `Download & Run` the code

#### Components

Component|No.|Source|Cost|Notes
--|--|--|--|--
Microusb data cable|1|Ebay|£1.20|
NodeMcu-CP2102-ESP8266 Development Board (narrow profile)|1|[AliExpress](https://www.aliexpress.com/item/32665100123.htm)|£1.93|
Jumper Wires|10|Ebay|£1|
Resistor 4.7k Ohm|1|Ebay|£0.50|
Conductive Yarn|1|Various|£1|
Pressure Sensor|1|Various|£1|
Conductive Rubber|1|Various|£1|
Textile Back|1|Various|£1|
TOTAL|||£8.63|


### Session 3

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electronics-green.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-python-black.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-terminals-lightblue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-esp8266-gold.svg?longCache=true&style=plastic)

Multiple Neopixel control and Re-visiting our sensor circuit but this time combine with our ESP8266 boards and controlling our LEDs


### Mutliple NeoPixels

```
from lights import *
```

You can run this example code from the [NeoPixel MicroPython Guide](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html):

Once the `lights.py` file is on board, re-log on to your board and you can run these commands:

`cycle()`, `bounce()`, `fade()` and `clear()`

There's also a [`main.py`](https://github.com/cheapjack/WearableTechBadge/blob/master/examples/circle/main.py) you can add so they run on booting the board.

Try writing your own combinations of these functions on a loop and try changing the for loops to cycle through colours


```
from machine import Pin
from neopixel import NeoPixel
import time

n = 7 # Set the number of pixels on your NeoPixel
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
```

### Sensor Readings

<img src="images/ESP8266-Schem-Fritzing.png" width="600">

Ok now lets read the values of one of our sensors. Wire up following the diagram above.

The ADC (analog to digital conversion) Pin is labelled A0 on your board and we will need the ADC class to make it work

`from machine import ADC`
`adc = ADC(0)`
`adc.read()`

Will return a value. Ok lets get it to read the values until we press `ctrl +c`. We will use a simple loop using `while`

`while True:` press return and you will see `...` and your cursor will indent automatically.

`adc.read()`

Now press return, and you get another indent, return a few time indicates thats the end of that loop and it will then execute the code.

Play with your sensor and watch the numbers change. Cool eh? Bit fast though, lets slow it down with `time`

`import time`

Now we can use `time.sleep(seconds)` to wait before reading the pin again.

```
while True:
    adc.read()
    time.sleep(0.5)
```

Now lets use that to blink our LED

```
while True:
    Led2.on()
    time.sleep_ms(adc.read() * 10)
    Led2.off()
    time.sleep_ms(adc.read() * 10)
```

Ok but higher resistance, bigger stretch or pressue is slowing our flashes. WE can flip it round

```
while True:
    stretch = 500 - (adc.read() *10)
    Led2.on()
    time.sleep_ms(stretch)
    Led2.off()
    time.sleep_ms(stretch)
```

### Session 4


![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-sewing-orange.svg?longCache=true&style=plastic)

Fabricate our amoeba shaped wearable badge and assemble everything using a textile pocket to enclose electronics

 * Enclose the ESP circuit in a customisable fabric template

### Additional Tutorials

### PWM output and Controlling LEDs

We've taken from [this tutorial by Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-esp8266-pwm-micropython/)

<img src="images/PWM_esp8266_Schem.png" width="400">

For this example, wire an LED to your ESP board. We’ll wire the LED to `GPIO 5` (marked as `D1` on your board), but you can choose another suitable PWM pin

Here’s the script that changes the LED brightness over time by increasing the duty cycle.

```
from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(5), frequency)

while True:
    for duty_cycle in range(0, 1024):
    led.duty(duty_cycle)
    sleep(0.005)
```

Also refer to these tutorials
 * [PWM Tutorial](https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html#pulse-width-modulation)
 * [Fading an LED](https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html#fading-an-led)

### Command Line alternatives to uPyCraft

Once you've got used to micropython there are soem command line options for advanced users that you can see below.

#### Using PUTTY

To get connected on Windows you could also use PUTTY

Windows Download [PuTTY](https://putty.org/) to connect your ESP8266 to your computer over USB-Serial and be able to send commands to control and set it up.

Open PuTTY and select `serial` and choose a COM port usually COM3 or COM7. Then change the baud rate to 115200 and leave the rest as defaults and select open. This will open a black screen with the python prompt `>>>`. You can now 'talk' to the board. Start with typing

```
print("hello!")
```
If you get hello printed on the next line you are all setup!

Linux - Use the built in `screen`, `minicom` or Putty using `$ sudo apt-get install putty` in your Linux Terminal. I'd recommend screen.

Mac - Download [PuTTY](https://putty.org/) or use the built-in `Applications/Terminal` and `screen`

#### Using `screen`

On macos and Linux you can just use a Terminal and `screen`. If your linux doesnt have screen install with `sudo apt-get install screen` or `brew install screen` on a mac after setting up [HomeBrew](https://brew.sh/)

`$ ls /dev/tty.*`

to list your usb devices.

`$ screen /dev/device-name baud-rate`
is the general format.

`$ screen -S wearable /dev/tty.SLAB_USBtoUART 115200`

Then press enter and you'll see the python prompt. You are now connected to your ESP8266!

### Making Permanent Changes

You need to make a `main.py` file on the board. To do this you need to write your code and copy it into the command line prompt of the ESP

So copy the text from [main.py](main.py).
Then in your open console for your ESP:

`f = open('main.py', 'w')`

then use **paste mode**: move your cursor to just after the set of 3 quotes (they are essential) and press `ctrl + e` and you will be given a few options: right click paste or shortcut `cmd + v` to paste in your text for the programme. Then finish and call `f.close()` to close and save the file.

```
f.write('''paste_your_text here''')
f.close()
```

Check its there with

`import os`
and
`os.listdir()` to check it's there.


Now reboot, and if your file is correct it will run the `boot.py` script (don't worry about that for now it just sets up the board and python) and then your `main.py` file should run!



### Ampy

There are other methods to upload more complex files you can look at like [ampy](https://github.com/scientifichackers/ampy) so we will try setting this up for you.

 * `ampy --port /dev/MY_PORT_NAME ls` Lists files

 * `ampy --port /dev/MY_PORT_NAME put examples/circle/lights.py` Puts the file on the board

 * `ampy --port /dev/MY_PORT_NAME rm examples/circle/lights.py` Removes the file on the board

## TODO

 * [x] Re-solder the press studs
