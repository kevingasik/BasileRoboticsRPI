import board
import neopixel 
pixels = neopixel.NeoPixel(board.D18, 5)
pixels[3] = (255, 0, 0)
#pixels.fill((0, 255, 0))


# import neopixel
# from board import *

# RED = 0x100000 # (0x10, 0, 0) also works

# pixels = neopixel.NeoPixel(NEOPIXEL, 10)
# for i in range(len(pixels)):
    # pixels[i] = RED
    

