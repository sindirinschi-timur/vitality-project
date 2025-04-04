import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Controls
button_up = Pin(7, Pin.IN, Pin.PULL_UP)    # SW0
button_down = Pin(9, Pin.IN, Pin.PULL_UP)  # SW2
button_clear = Pin(8, Pin.IN, Pin.PULL_UP) # SW1

# Draw Vars
draw_x = 0
draw_y = HEIGHT // 2
draw = True

def clear():
    oled.fill(0)
    oled.show()

def drawing():
    oled.pixel(draw_x, draw_y, 1)
    oled.show()

def main():
    global draw_x, draw_y, draw
    
    clear()
    
    while True:
        draw_x += 1
        if draw_x >= WIDTH:
            draw_x = 0

        if button_up.value() == 0 and draw_y > 0:
            draw_y -= 1
            time.sleep(0.01)
            
        if button_down.value() == 0 and draw_y < HEIGHT - 1:
            draw_y += 1
            time.sleep(0.01)
            
        if button_clear.value() == 0:
            clear()
            draw_x = 0
            draw_y = HEIGHT // 2
            time.sleep(0.2)
        
        drawing()
        time.sleep(0.01)  # Controls the speed (lower is faster)

if __name__ == "__main__":
    main()