"""
This example shows connecting to the PN532 with I2C (requires clock
stretching support), SPI, or UART. SPI is best, it uses the most pins but
is the most reliable and universally supported.
After initialization, try waving various 13.56MHz RFID cards over it!
"""
import time
import RPi.GPIO as GPIO

from pn532 import *

from LEDControl import LEDControl
import buzzer



if __name__ == '__main__':
    
    led_strip = LEDControl()
    buzzer.init()
    
    
    try:
        pn532 = PN532_SPI(debug=False, reset=20, cs=4)


        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print('Waiting for RFID/NFC card...')
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print('.', end="")
            # Try again if no card is available.
            if uid is None:
                continue
            print('Found card with UID:', [hex(i) for i in uid])
            uid=bytes(uid)
            buzzer.beep()
            if(uid[-2]==0x85):
                led_strip.blinkGreen()
            else:
                led_strip.blinkRed()
            time.sleep(0.1)
            led_strip.turnOff()
            
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()
