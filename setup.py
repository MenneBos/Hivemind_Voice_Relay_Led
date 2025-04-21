from setuptools import setup, find_packages

setup(
    name='hivemind_voice_relay_led',
    version='0.1',  # Pas dit aan naar je versie
    packages=find_packages(),  # Dit zoekt naar alle pakketten in de huidige map
    install_requires=[
        'ovos-bus-client',  # Vereiste dependencies
        'RPi.GPIO',
        'ovos-utils',
    ],
    entry_points={
        'console_scripts': [
            'hivemind-voice-relay-led = hivemind_voice_relay_led.__main__:main',  # Dit maakt de CLI beschikbaar
        ]
    },
    include_package_data=True,  # Zorg ervoor dat alle nodige bestanden worden meegenomen
)