# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:28:35 2018

@author: alumno
"""
import sys
import smallsmilhandler
import json
import urllib.request
from xml.sax import make_parser


class KaraokeLocal:

    def __init__(self, file):
            handler = smallsmilhandler.SmallSMILHandler()
            parser = make_parser()
            parser.setContentHandler(handler)
            parser.parse(open(file))
            self.etiqs = handler.get_tags()

    def __str__(self):
        data = ''
        for line in self.etiqs:
            for atrib in line:
                if line[atrib] != "":
                    data += atrib + "=" + "'" + line[atrib] + "'" + '\t'
            data += '\n'
        return data

    def to_json(self, file, fich_json=None):

        if fich_json is None:
            fich_json = file.split('.')[0] + '.json'
        json.dump(self.etiqs, open(fich_json, "w"))

    def do_local(self):

        for line in self.etiqs:
            for atrib in line:
                if line[atrib][0:7] == 'http://':
                    direction = line[atrib].split('/')[-1]
                    urllib.request.urlretrieve(line[atrib])
                    line[atrib] = direction

if __name__ == '__main__':

    try:
        file = sys.argv[1]
        karaoke = KaraokeLocal(file)

    except IndexError:
        sys.exit('usage error: python3 karaoke.py file.smil')
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    karaoke.to_json(file, 'local.json')
    print(karaoke)
