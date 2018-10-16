#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):

        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.todo = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background_color', "")
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")

    def get_tags(self):
        return self.todo

if __name__ == "__main__":
    parser = make_parser()
    SmilHandler = SmallSMILHandler()
    parser.setContentHandler(SmilHandler)
    parser.parse(open('karaoke.smil'))
