import urllib.request
import re
import requests
import openpyxl
import urllib.parse
from urllib.parse import quote
from urllib import request,error
from bs4 import BeautifulSoup
from openpyxl import workbook
import xlwt
from lxml import etree
from pyquery import PyQuery as pq
def open_url(i):

        req = urllib.request.Request(i)
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        page = urllib.request.urlopen(req)
        html = page.read().decode('utf-8')
        return html

def get_data(html):
    '''
    soup = BeautifulSoup(html,'lxml')
    m = soup.find(class_="lemma-summary")
   file = open('简介.txt','a',encoding='utf-8')
   for i in m.div.children:
        file.write(''.join([i.string]))
    file.write("\n")'''
    global ws
    title = []

    doc = pq(html)
    items = doc('.lemma-summary')
    lis = items.children()
    try:
     lis.find('sup').remove()
     print(lis.text())
    except:
        pass
    title.append(lis.text())
    ws.append(title)


if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['简介'])
    urls = []
    with open('1.txt') as f:
        for eachline in f:
            url = "https://baike.baidu.com/item/" + quote(eachline)
            urls.append(url.replace('%0A',''))

    for i in urls:
        try:
            get_data(open_url(i))
        except:
            ws.append(['该词条不存在'])
            print('该词条不存在')
        finally:
            wb.save('test.xlsx')



''' for i in urls:
        try:
            get_title(open_url(i))
            print(i)
        except:
            print('该词条不存在')
            file = open('简介.txt', 'a', encoding='utf-8')
            file.write("该词条不存在\n")
'''











