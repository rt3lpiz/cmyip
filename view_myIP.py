# coding: utf-8
from easygui import msgbox
from urllib import urlopen
from lxml import html
def main():
    tree = html.document_fromstring(urlopen('http://cmyip.org').read())
    ip = tree.xpath('//h1[@class="page-title"]/b')
    msgbox(msg=ip[0].text)
if __name__ == '__main__':
    main()
