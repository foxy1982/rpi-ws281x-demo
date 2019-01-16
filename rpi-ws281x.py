from rpi_ws281x import *
import time

LED_COUNT = 30      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN)
    strip.begin()

    i = 0
    while True:
        for j in range(0, strip.numPixels(), 1):
            strip.setPixelColor(j, Color(0, 0, 0))
        strip.setBrightness(i * 8 + 10)
        strip.setPixelColor(i, Color(0, 0, 255))
        strip.show()
        i = i + 1
        
        if (i == LED_COUNT):
            i = 0
        
        time.sleep(0.1)
