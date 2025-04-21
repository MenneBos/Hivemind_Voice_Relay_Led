import atexit
import RPi.GPIO as GPIO
from ovos_utils.log import LOG  # OVOS logging importeren
from hivemind_voice_relay.service import get_bus
from ovos_bus_client.message import Message

LED_PIN = 17 

# Setup GPIO
GPIO.setmode(GPIO.BCM)   #zorgt voor Broadcom nummer dus GPIO 17
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Zorg dat LED uit is bij start

# Cleanup-functie voor veilig afsluiten
def cleanup():
    GPIO.output(LED_PIN, GPIO.LOW)  # Zet LED uit
    GPIO.cleanup()                  # Geef alle GPIO-pinnen vrij

# Registreer cleanup-functie
atexit.register(cleanup)

# Functie om logberichten te geven wanneer bus goed werkt
def bus_ready_callback(message: Message):
    # Hier is 'message' het bericht dat de bus verstuurt naar deze callback
    LOG.info("HiveMind bus succesvol verbonden en werkt!")

def on_start_listening(message: Message):
    # 'message' bevat de informatie die door de bus wordt verstuurd
    LOG.info("Bericht ontvangen: recognizer_loop:record_begin")
    GPIO.output(LED_PIN, GPIO.HIGH)  # LED aan

def on_end_listening(message: Message):
    # 'message' bevat de informatie die door de bus wordt verstuurd
    LOG.info("Bericht ontvangen: recognizer_loop:record_end")
    GPIO.output(LED_PIN, GPIO.LOW)   # LED uit

# Als script direct wordt uitgevoerd, start de bus en luister naar berichten
if main():
    try:
        bus = get_bus()  # Haalt de HiveMessageBusClient op via de get_bus functie
        bus.on("recognizer_loop:record_begin", on_start_listening)
        bus.on("recognizer_loop:record_end", on_end_listening)
        bus.on("hivemind_bus:ready", bus_ready_callback)  # Bus is klaar

        LOG.info("Verbinding met de HiveMind bus is succesvol!")
        bus.run_forever()

    except Exception as e:
        LOG.error(f"Fout bij verbinden met de HiveMind bus: {e}")
