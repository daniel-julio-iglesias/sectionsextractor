"""
GNU+Health%2FFamilies
GNUHealthFamilies.html
https://en.wikibooks.org/wiki/GNU_Health/Families

exampleSoup.select('p')
exampleSoup.select('h1')
exampleSoup.select('h2')
"""
import os
import codecs
import math
from config import basedir
import requests, bs4
from app import http_proxy, https_proxy


class HTMLSectionsExtractor:
    def __init__(self, trainingdir, inputdoc):
        filename = trainingdir + inputdoc
        # self.f = open(filename)
        self.f = codecs.open(filename, 'r', 'iso8859-1')
        # print(self.f.readline())

        """ self.proxies = {
            'http': 'http://user:pass@proxyAddress:proxyPort',
            'https': 'http://user:pass@proxyAddress:proxyPort0',
        }
        """

        self.proxies = {
            'http': http_proxy,
            'https': https_proxy,
        }

        print('http_proxy: ', http_proxy)

        self.res = requests.get('https://en.wikibooks.org/wiki/GNU_Health/Families')
        # self.res = requests.get('https://en.wikibooks.org/wiki/GNU_Health/Families', proxies=self.proxies)

        if self.res.status_code == requests.codes.ok:
            # self.gnuHealthSoup = bs4.BeautifulSoup(self.res.text)
            self.gnuHealthSoup = bs4.BeautifulSoup(self.res.text, "html.parser")

    def extract(self):
        # content = self.f.readline()
        content = None

        if not isinstance(self.gnuHealthSoup, bs4.BeautifulSoup):
            return content
        else:
            content = ''

        h1Elems = self.gnuHealthSoup.select('h1')
        str(h1Elems[0])
        content = content + ' ' + h1Elems[0].getText()   # TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

        h2Elems = self.gnuHealthSoup.select('h2')
        str(h2Elems[0])
        content = content + ' ' + h2Elems[0].getText()

        pElems = self.gnuHealthSoup.select('p')
        str(pElems[0])
        content = content + ' ' + pElems[0].getText()

        # print(content)
        return content


if __name__ == '__main__':
    # training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train')
    training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train', '00010Preface')
    training_dir = training_dir + os.sep
    doc = '01.txt'
    hse = HTMLSectionsExtractor(training_dir, doc)
    print(hse.extract())
