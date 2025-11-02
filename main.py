import dht  # type: ignore
from machine import Pin  # type: ignore
import time

def read_dht22(sensor):
    """
    Liest Temperatur und Luftfeuchtigkeit von einem DHT22-Sensor aus.
    Gibt ein Tupel (Temperatur, Luftfeuchtigkeit) zurück.
    Bei Fehler: (None, None)
    """
    try:
        sensor.measure()               # Sensor auslesen
        temp = sensor.temperature()    # Temperatur abrufen
        hum = sensor.humidity()        # Luftfeuchtigkeit abrufen
        return temp, hum
    except OSError as e:
        print("Fehler beim Auslesen des Sensors:", e)
        return None, None

# Hauptfunktion
def main():
    sensor = dht.DHT22(Pin(2))
  
    while True:
        temp, hum = read_dht22(sensor)
        if temp is not None:
            print(f"Temperatur: {temp:.1f}°C, Luftfeuchtigkeit: {hum:.1f} %")
        time.sleep(2)

# "Startpunkt" des Programms
if __name__ == "__main__":
    main()