from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(14))

while True:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
