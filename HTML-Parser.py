from bs4 import BeautifulSoup
import requests
data=[]
currencies=[]
url_2 = 'https://tr.wikipedia.org/wiki/En_çok_kullanılan_para_birimleri_listesi'
sayfa_2 = requests.get(url_2)
html_sayfa_2 = BeautifulSoup(sayfa_2.content, "html.parser")
# wikitable sortable jquery-tablesorter
table = html_sayfa_2.find('table', class_="wikitable")
table_body = table.find('tbody')

rows = table_body.findAll('tr')
for row in rows:
    cols = row.findAllNext('td')

cols = [ele.text.strip() for ele in cols]
data.append([ele for ele in cols if ele])

print(data)
print("---------------\n-----------")


a=6

while a <=len(data[0]):
    print(data[0][a-1 ]+data[0][a]+"  " +data[0][a+1])

    if data[0][a]=="Meksika pesosu":
        break

    a+=4