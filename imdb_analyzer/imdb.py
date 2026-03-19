import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/toptv/?ref_=hm_nv_menu"
headers= {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) APPLEwEBkİT/537.36 (KHTML, like Gecko) Chrome 119.0.0.0"
}
html=requests.get(url,headers=headers).content
soup=BeautifulSoup(html,"html.parser")

liste=soup.find("ul",{"class": "ipc-inline-list base"}).find_all("li",limit=10)
for item in liste:
    filmadi=item.find("h3",{"class":"ipc-inline-list base"})
    print(filmadi)
    puan=item.find("span",{"class":"ipc-rating-star"})
print(filmadi,puan)
