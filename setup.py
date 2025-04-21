from setuptools import setup, find_packages

def get_version():
    """ Find the version of this skill"""
    version_file = os.path.join(os.path.dirname(__file__), 'hivemind_voice_relay_led', 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if int(alpha):
        version += f"a{alpha}"
    return version

setup(
    name='hivemind_voice_relay_led',
    version=get_version(),
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