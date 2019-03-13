import pycom
from machine import Pin
import time
import machine

def main():
    pycom.heartbeat(False)


    p_in2 = Pin('G6', mode=Pin.OUT)
    p_in2.value(0)
    time.sleep(1)
    p_in2.value(1)

    adc = machine.ADC()
    apin = adc.channel(pin='G3')
    while True:
        val = apin.voltage()
        temp = (val - 500) / 10
        print(temp)
        time.sleep(0.1)
    



if __name__ == '__main__':
    main()
