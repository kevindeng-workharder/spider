
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bf
html = urlopen("http://www.baidu.com/")
obj = bf(html.read(),'html.parser')
title = obj.head.title
print(title)
