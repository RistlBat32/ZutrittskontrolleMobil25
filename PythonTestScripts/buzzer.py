# GPIO-Bibliothek laden
import RPi.GPIO as GPIO
import time

BUZZER_PIN=23


def init():
    
    # BCM-Nummerierung verwenden
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def beep():

    GPIO.output(BUZZER_PIN, True)
    time.sleep(0.2)
    GPIO.output(BUZZER_PIN, False)
