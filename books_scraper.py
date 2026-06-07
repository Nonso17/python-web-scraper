import requests
from bs4 import BeautifulSoup
import csv

with open('books.csv','w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Title','Price','Availability'])
    page=1

    while True:
        url=f'https://books.toscrape.com/catalogue/page-{page}.html'
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        books=soup.find_all('article',class_='product_pod')

        if not books:
            break
        for book in books:
            title=book.h3.a['title']
            price=book.find('p',class_='price_color').text
            availability=book.find('p',class_='instock availability').text.strip()
            writer.writerow([title,price,availability])
            page +=1
    print("Successful")
