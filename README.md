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
2. Install python modules listed in requirements.txt <br>```pip3 install -r requirements.txt```,
3. Install Julius 4.4.2 and Julius Japanese Dictation Kit 4.4,
4. Run julius in modeule mode,
5. Run controller module<br>```python3 controller.py```.

# Configure controller

You can configure controller by editting settings.toml.

## Specify Julius host and port

```
host = 'yourhost.example.com'
port = 12345
```
## Add new commands

```
[[commands]]
words = ['Word1', 'Word2', 'Word3']
file = 'name_of_your_command.sh'
```

Note: Julius shoud be able to recognize the words.
