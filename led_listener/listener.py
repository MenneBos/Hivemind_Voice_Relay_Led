import RPi.GPIO as GPIO
import atexit
from ovos_bus_client.message import Message
from hivemind_voice_relay.service import get_bus  # 👈 rechtstreeks uit je package

# 🔌 GPIO setup
LED_GPIO = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)
GPIO.output(LED_GPIO, GPIO.LOW)

def cleanup():
    GPIO.output(LED_PIN, GPIO.LOW)  # Zet LED uit
    GPIO.cleanup()                  # Geef alle GPIO-pinnen vrij
    
atexit.register(GPIO.cleanup)

# 🎙️ Callback handlers
def on_listen_start(msg: Message):
    GPIO.output(LED_GPIO, GPIO.HIGH)
    print("🎙️ LED ON - Listening started")

def on_listen_end(msg: Message):
    GPIO.output(LED_GPIO, GPIO.LOW)
    print("🔇 LED OFF - Listening ended")

def main():
    bus = get_bus()  # Verbindt automatisch met juiste sleutel, host etc.
    bus.on("recognizer_loop:record_begin", on_listen_start)
    bus.on("recognizer_loop:record_end", on_listen_end)
    print("🔌 LED listener connected to HiveMind MessageBus")
    bus.run_forever()

if __name__ == "__main__":
    main()