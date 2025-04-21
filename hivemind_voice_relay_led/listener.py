import RPi.GPIO as GPIO
from ovos_simple_listener import ListenerCallbacks
from ovos_utils.log import LOG
import time

# Stel GPIO in
LED_PIN = 17  # Verander dit naar de juiste GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Callback implementatie voor de listener
class MyCallbacks(ListenerCallbacks):
    @classmethod
    def listen_callback(cls):
        # Deze callback wordt aangeroepen wanneer de listener start
        LOG.info("Listener gestart!")
        GPIO.output(LED_PIN, GPIO.HIGH)  # Zet de LED aan
        LOG.info("LED aan")

    @classmethod
    def end_listen_callback(cls):
        # Deze callback wordt aangeroepen wanneer de listener stopt
        LOG.info("Listener gestopt!")
        GPIO.output(LED_PIN, GPIO.LOW)  # Zet de LED uit
        LOG.info("LED uit")

    @classmethod
    def audio_callback(cls, audio):
        # Deze callback wordt aangeroepen wanneer audio wordt verwerkt
        LOG.info("Audio ontvangen voor verwerking")

    @classmethod
    def error_callback(cls, audio):
        # Deze callback wordt aangeroepen bij een fout tijdens STT (Speech To Text)
        LOG.error("Fout bij STT verwerking")

    @classmethod
    def text_callback(cls, utterance, lang):
        # Deze callback wordt aangeroepen wanneer tekst wordt herkend
        LOG.info(f"Herkenning van tekst: {utterance}")

# Start de listener (voorbeeld)
def main():
    from ovos_simple_listener import SimpleListener
    listener = SimpleListener(callbacks=MyCallbacks)
    listener.start()

if __name__ == '__main__':
    main()
