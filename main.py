import dht # type: ignore
from machine import Pin # type: ignore
import time

# Sensor an GPIO4, DHT11
sensor = dht.DHT11(Pin(4))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperatur: {temp} °C, Luftfeuchtigkeit: {hum} %")
    except OSError as e:
        print("Fehler beim Lesen des Sensors:", e)
    time.sleep(2)