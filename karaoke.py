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

if __name__ == "__main__":

    try:
        karaoke = KaraokeLocal(sys.argv[1])

    except IndexError:
        sys.exit('usage error: python3 karaoke.py file.smil')
    print(karaoke)
