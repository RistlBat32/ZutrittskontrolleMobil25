# GPIO-Bibliothek laden
import RPi.GPIO as GPIO
import time

BUZZER_PIN=13


def init():
    
    # BCM-Nummerierung verwenden
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def beep(duration=0.2):
    GPIO.output(BUZZER_PIN, True)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, False)


if __name__ == "__main__":
    init()
    beep()
