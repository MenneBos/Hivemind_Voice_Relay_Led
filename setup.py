from setuptools import setup, find_packages
import os
from os import walk, path
from os.path import join, dirname
from pathlib import Path

version_ns = {}
exec(Path("version.py").read_text(), version_ns)

setup(
    name='hivemind_voice_relay_led',
    version=version_ns["__version__"],
    packages=find_packages(),  # Dit zoekt naar alle pakketten in de huidige map
    install_requires=[
        'ovos-bus-client',  # Vereiste dependencies
        'RPi.GPIO',
        'ovos-utils',
    ],
    entry_points={
        'console_scripts': [
            'hivemind-voice-relay-led = hivemind_voice_relay_led.__main__:run',  # Dit maakt de CLI beschikbaar
        ]
    },
    include_package_data=True,  # Zorg ervoor dat alle nodige bestanden worden meegenomen
)