import requests
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
html=requests.get(url,headers=headers).content
soup=BeautifulSoup(html,"html.parser")
books = soup.find_all("article", class_="product_pod",limit=100)
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"Kitap: {title} - Fiyat: {price}")