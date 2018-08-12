# -*- coding: utf-8 -*-
import sys
import codecs
from html.parser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'onclick':
                    self.recording = 1
        else:
            self.recording = 0

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)

text_file = open("test.html", "r",encoding="utf8")
content = text_file.readlines()
content = [x.strip() for x in content]

soup = BeautifulSoup(content, 'html.parser')

print(soup.prettify())


#parser = MyHTMLParser()
#parser.feed(str(content))
#print(parser.data)
#parser.close()