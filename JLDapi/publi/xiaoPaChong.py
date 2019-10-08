# _*_ coding:utf-8 _*_
import re
import urllib.request

url = "http://www.baofeng.com/tv.html"


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = str(page.read())
    return html


def getImg(html):
    reg = r'data-pic="(.+?\.jpg)"'
    imgre = re.compile(reg)
    piclist = re.findall(imgre, html)
    print(piclist)
    for i in range(len(piclist)):
        urllib.request.urlretrieve(piclist[i], '%s.jpg' % i)


html = getHtml(url)
getImg(html)

