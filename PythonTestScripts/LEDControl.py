import time

from rpi_ws281x import Color, PixelStrip, ws
import buzzer

# LED self.strip configuration:
LED_COUNT = 16         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = True      # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW


class LEDControl:   
    
    def __init__(self):
         # Create NeoPixel object with appropriate configuration.
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    
            
    # Define functions which animate LEDs in various ways.
    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
    
    def blinkGreen(self):
        for i in range(self.strip.numPixels()//2):
            self.strip.setPixelColor(i, Color(255, 0, 0))
            self.strip.setPixelColor(16-i, Color(255, 0, 0))
            self.strip.show()
            time.sleep(0.05)
        
    def blinkRed(self):
        for i in range(self.strip.numPixels()//2):
            self.strip.setPixelColor(i, Color(0, 255, 0))
            self.strip.setPixelColor(16-i, Color(0, 255, 0))
            self.strip.show()
            time.sleep(0.02)
        for i in range(5):
            self.turnOff()
            time.sleep(0.2)
            for i in range(self.strip.numPixels()//2):
                self.strip.setPixelColor(i, Color(0, 255, 0))
                self.strip.setPixelColor(16-i, Color(0, 255, 0))
            self.strip.show()
            buzzer.beep()
            
        
        
    def turnOff(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

    
    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, color)
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)
    
    
    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
    
    
    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((i + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
    
    
    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel(((i * 256 // self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
    
    
    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, wheel((i + j) % 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)
            
    
    
# Main program logic follows:
if __name__ == '__main__':
    strip = LEDControl()
    
    print('Press Ctrl-C to quit.')
    while True:
        # Color wipe animations.
        strip.colorWipe(Color(255, 0, 0))  # Red wipe
        strip.colorWipe(Color(0, 255, 0))  # Blue wipe
        strip.colorWipe(Color(0, 0, 255))  # Green wipe
        strip.colorWipe(Color(0, 0, 0, 255))  # White wipe
        strip.colorWipe(Color(255, 255, 255))  # Composite White wipe
        strip.colorWipe(Color(255, 255, 255, 255))  # Composite White + White LED wipe
        # Theater chase animations.
        strip.theaterChase(Color(127, 0, 0))  # Red theater chase
        strip.theaterChase(Color(0, 127, 0))  # Green theater chase
        strip.theaterChase(Color(0, 0, 127))  # Blue theater chase
        strip.theaterChase(Color(0, 0, 0, 127))  # White theater chase
        strip.theaterChase(Color(127, 127, 127, 0))  # Composite White theater chase
        strip.theaterChase(Color(127, 127, 127, 127))  # Composite White + White theater chase
        # Rainbow animations.
        strip.rainbow()
        strip.rainbowCycle()
        strip.theaterChaseRainbow()
