# voice_controller

A module executing commands through voice.

Note: It is a development version.

# Dependencies

| Name   | Version    |
|:-----:|:-----------:|
| [Python](https://www.python.org/) | 3.6 |
| [Julius](https://github.com/julius-speech/julius) | 4.4.2      |
| [Julius Japanese Dictation Kit](https://github.com/julius-speech/dictation-kit) | 4.4 |

# Setup and run

1. Install python 3.6,
2. Install python modules listed in requirements.txt (pip3 install -r requirements.txt),
3. Install Julius 4.4.2 and Julius Japanese Dictation Kit 4.4,
4. Run julius in modeule mode,
5. Run controller module (python3 controller.py)

# configure controller

You can configure controller by editting settings.toml.

## Specify Julius host and port

'''code
host = 'localhost'
port = 10500
'''
