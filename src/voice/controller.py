'''
Copyright 2018 Morning Project Samurai                                                           

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
to permit persons to whom the Software is furnished to do so, subject to the following conditions:                                                 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of 
the Software.                                                                   

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


import os
import subprocess
import time
import socket
import bs4
import toml


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


try:
    BASE_DIR = os.environ['NEOCHI_HOME']
except KeyError:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, 'settings.toml')
COMMANDS_DIR = os.path.join(BASE_DIR, 'commands')


class VoiceController:
    
    def __init__(self):
        self._settings = toml.load(SETTINGS_PATH)
        self._active = False

    @property
    def is_active(self):
        return self._active

    def connect(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._settings['voice']['host'], self._settings['voice']['port']))
                
    def start(self):
        data = ''
        start_time = -1
        while True:
            if '</RECOGOUT>\n' in data:
                html = bs4.BeautifulSoup(data)
                whypos = html.findAll('whypo')
                if not whypos or float(whypos[0]['cm']) < self._settings['voice']['recognition_th']:
                    data = ''
                    continue
                word = whypos[0]['word']
                if not self.is_active and word in self._settings['voice']['activation']:
                    print('Activated')
                    self._active = True
                    start_time = time.time()
                elif self.is_active:
                    for command in self._settings['voice']['commands']:
                        if word in command['words']:
                            subprocess.run(os.path.join(COMMANDS_DIR, command['file']))
                            self._active = False
                            break
                data = ''
            else:
                data += self._client.recv(1024).decode()
            if self.is_active and time.time() - start_time > self._settings['voice']['timeout']:
                print('Timeout')
                self._active = False
                
    def close(self):
        self._client.close()
    

if __name__ == '__main__':
    try:
        vc = VoiceController()
        vc.connect()
        vc.start()
    except KeyboardInterrupt:
        vc.close()
    
