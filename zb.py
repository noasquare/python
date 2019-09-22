import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import re

res = requests.get("http://www.weain.mil.cn/wzgg/")
res.raise_for_status()

# 找到第一条链接，并点击打开到新的页面。
soup = BeautifulSoup(res.text,"html.parser")
target = soup.select("dt a")
new_target = target[0].get('href')
# print(new_target)

new_link = "http://www.weain.mil.cn" + new_target
# 在页面里寻找“天线罩”，并返回寻找的结果，没有也要返回。
res_target = requests.get(new_link)
res_target.encoding = 'utf-8'  #这句的作用是，让中文正常显示，通过查看网页的meta得知编码方式为utf-8
res_target.raise_for_status()
soup_target = BeautifulSoup(res_target.text,"html.parser")

# key_word1 = '天线罩'
key_word1 = '天线'
result = soup_target.body.findAll(text=re.compile(key_word1))
if len(result):
    output1 = '你要的',key_word1,'项目，来了',result,'详细地址请点击：',new_link
    print(output1)
else:
    output2 = '没有你要的'+key_word1+'项目!'