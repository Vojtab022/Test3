import machine
import time

tlacitko = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)

led_pins = [1, 2, 3]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

stav = 0 
minulý_stav = 0 

while True:
    aktuální_stav = tlacitko.value() 

    if aktuální_stav == 1 and minulý_stav == 0:
        stav = (stav + 1) % 4 
        print(f"Stav: {stav}")
        
        if stav == 0:
            for led in leds:
                led.value(0)
        elif stav == 1:
            for led in leds:
                led.value(1)
        elif stav == 2:
            for i in range(5):
                for led in leds:
                    led.value(1)
                time.sleep(0.5)
                for led in leds:
                    led.value(0)
                time.sleep(0.5)
        elif stav == 3:
            for i in range(10):
                for j in range(3):
                    leds[j].value(1)
                    time.sleep(0.5)
                    leds[j].value(0)
                    time.sleep(0.5)

    minulý_stav = aktuální_stav 
    time.sleep(0.1) 
