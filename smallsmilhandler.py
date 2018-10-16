#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.etiq_atrib = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']}
        self.etiqs = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.etiq_atrib:
            atribs = {}
            atribs['etiq'] = name
            for atrib in self.etiq_atrib[name]:
                atribs[atrib] = attrs.get(atrib, "")
            self.etiqs.append(atribs)

    def get_tags(self):
        return self.etiqs

if __name__ == "__main__":
    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open('karaoke.smil'))
    print(handler.get_tags())
