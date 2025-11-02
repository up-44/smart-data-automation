import dht  # type: ignore
from machine import Pin  # type: ignore
import time

# DHT22 Sensor an GPIO 2
sensor = dht.DHT22(Pin(2))  # type: ignore

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity() 
        print(f"Temperatur: {temp:.1f} °C, Luftfeuchtigkeit: {hum:.1f} %")
    except OSError as e:
        print("Fehler beim Auslesen des Sensors:", e)
    time.sleep(2)  # alle 2 Sekunden messen