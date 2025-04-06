import time
import RPi.GPIO as GPIO
import requests
import json

from pn532 import *
from LEDControl import LEDControl
import buzzer

# Ziel-URL der Checkin-API
API_URL = "http://localhost:8000/api/checkin/"
INTERRUPT_PIN = 16

if __name__ == '__main__':
    led_strip = LEDControl()
    buzzer.init()
    GPIO.setup(INTERRUPT_PIN, GPIO.IN) #pull_up_down=GPIO.PUD_UP

    try:
        pn532 = PN532_SPI(debug=False, reset=20, cs=4)
        ic, ver, rev, support = pn532.get_firmware_version()
        pn532.SAM_configuration()

        while True:
            
            #This would be the three lines to enable interrrupts, However, this creates a higher CPU load. 
            pn532.start_auto_poll()
            if(GPIO.input(INTERRUPT_PIN)):
                GPIO.wait_for_edge(INTERRUPT_PIN, GPIO.FALLING)
            uid = pn532.read_autopoll_answer()
         

            #uid = pn532.read_passive_target(timeout=0.5)
            #print('.', end="", flush=True)
            if uid is None:
                continue

            uid_str = ''.join('{:02X}'.format(x) for x in uid)  # UID als Hex-String, z.B. "04AABBCCDD"

            buzzer.beep()
            led_strip.blinkWhite()

            # POST Request an die API
            try:
                response = requests.post(
                    API_URL,
                    headers={"Content-Type": "application/json"},
                    data=json.dumps({"nfc_id": uid_str})
                )

                result = response.json()
                message_type = result.get("message_type", "")

                # LED je nach Antwort
                if response.status_code != 200:
                    led_strip.blinkRed()

                if message_type == "success":
                    led_strip.blinkGreen()

                if message_type == "info":
                    led_strip.blinkBlue()

                if message_type == "warning":
                    led_strip.blinkYellow()

            except Exception as e:
                led_strip.blinkRed()

            time.sleep(0.1)
            led_strip.turnOff()

    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()
