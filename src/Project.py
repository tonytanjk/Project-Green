#hydroponics system 

import time
from threading import Thread
import queue

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_adc as adc
from hal import hal_buzzer as buzzer
from hal import hal_keypad as keypad
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_input_switch as input_switch
from hal import hal_ir_sensor as ir_sensor
from hal import hal_rfid_reader as rfid_reader
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_usonic as usonic
from hal import hal_dc_motor as dc_motor
from hal import hal_accelerometer as accel
lcd = LCD.lcd()
lcd.lcd_clear()

def main():
    ...

def pH_level(): # Determine pH level of Soil ()
    print("Write Code Here")

def amb_temp_humi(): # Grab Ambient Temperature and humidity to determine if fan need to be activated
    temperature, humidity = temp_humid_sensor.read_temp_humidity()
    lcd.lcd_display_string("Temperature "  +str(temperature), 1)  
    lcd.lcd_display_string("Humidity "  +str(humidity), 2)
    time.sleep(2)
    return temperature, humidity


def amb_light_intensity(): # Surrounding light intensity (controlling UV lights)
    print("Write Code Here")

def EC_level(): # Determine EC level and see if needed to release more or less nutrient solution
    print("Write Code Here")

def main_web(): #Dashboard to gather all sensor inputs
    print("Write Code Here")

def main(): # Main Function
    amb_temp()

if __name__ == "__main__":
    main()