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

# print(new_link)


# 在页面里寻找“天线罩”，并返回寻找的结果，没有也要返回。
res_target = requests.get(new_link)
res_target.encoding = 'utf-8'  #这句的作用是，让中文正常显示，通过查看网页的meta得知编码方式为utf-8
res_target.raise_for_status()
# soup_target = BeautifulSoup(res_target.text,"html.parser")
soup_target = BeautifulSoup(res_target.text,"html.parser")
# money = soup_target.select("td span")
# test_1 = money[6].getText()
# # print(test_1)
# playFile = open('test1.txt','w')
# playFile.write(test_1)
# playFile.close()
result = soup_target.body.findAll(text=re.compile('电缆'))
print(result)

table = soup_target.find("table")
rows = table.findAll('tr')
# print(len(rows[0].findAll("td")))
wb = Workbook()
ws = wb.active

for tr in rows:
    data = [r.getText() for r in tr.findAll("td")] # 先得到一个行数组，然后就可以把行数组赋值给append 函数。
    # print(data)
    ws.append(data)

ws.auto_filter.ref = ws.dimensions
ws.auto_filter.add_filter_column(0, ["电缆"])
wb.save("test.xlsx")
# 如何把找到的数据文件，转化为excel表格，然后利用excel表格的搜索功能，找到这个数据并发送给手机短信。2019年09月22日21:13:45
# playFile = open('test.txt','w')
# playFile.write(str(data))
# playFile.close()

