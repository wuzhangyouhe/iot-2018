import LCD2
import get_data_functions as func
import time

def display():
    LCD2.lcd_init()
    LCD2.lcd_string("CPU Usage: %s%%"%func.get_cpu_usage(),LCD2.LCD_LINE_1)
    LCD2.lcd_string("CPU Temp: %s"%func.get_cpu_temp(),LCD2.LCD_LINE_2)
    LCD2.lcd_string("RAM Usage: %s%%"%func.get_ram_usage(),LCD2.LCD_LINE_3)
    time.sleep(1)

def test():    
    try:
        while 1:
            display()
            time.sleep(0.05)
    finally:
        LCD2.lcd_clear()

test()