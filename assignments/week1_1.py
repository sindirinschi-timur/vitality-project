import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Buttons
right = Pin(7, Pin.IN, Pin.PULL_UP)  # SW0
left = Pin(9, Pin.IN, Pin.PULL_UP)   # SW2

# UFO Vars
ufo = " <=> " 
char = 8
ufo_width = len(ufo) * char
ufo_x = (WIDTH - ufo_width) // 2
ufo_y = HEIGHT - char
min_x = 0
max_x = WIDTH - ufo_width
last_press = 0
delay = 100 # Controls UFO speed (faster if lower)

def draw_ufo():
    oled.fill(0)
    oled.text(ufo, ufo_x, ufo_y)
    oled.show()

def is_button_pressed(pin):
    global last_press
    new_press = time.ticks_ms()
    
    if pin.value() == 0:
        if time.ticks_diff(new_press, last_press) > delay:
            last_press = new_press
            return True
    return False

def main():
    global ufo_x
    
    draw_ufo()
    
    while True:
        if is_button_pressed(right):
            if ufo_x < max_x:
                ufo_x += char
                draw_ufo()
        
        if is_button_pressed(left):
            if ufo_x > min_x:
                ufo_x -= char
                draw_ufo()
        
        time.sleep(0.01)

main()