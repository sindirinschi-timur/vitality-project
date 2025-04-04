import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

font = 8
max_lines = HEIGHT // font
lines = []
line = 0

def write_text():
    oled.fill(0)
    
    for i, line in enumerate(lines[-max_lines:]):
        oled.text(line, 0, i * font)
    
    oled.show()

def main():
    global line
    print("Hey! Type in terminal.")
    
    while True:
        user_input = input()
        lines.append(user_input)
        
        if len(lines) > max_lines:
            lines.pop(0)

        write_text()

if __name__ == "__main__":
    main()