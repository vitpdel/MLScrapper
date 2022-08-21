from itertools import product
import  os, sys
from    bs4 import  BeautifulSoup
import  requests


def scrap():
    URL =   input("Please, enter the product url: ")
    
    #This makes scraping work with any browser
    headers =   {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

    html  =   requests.get(URL,    headers=headers)
    soup    =   BeautifulSoup(html.text, "html.parser")

    try:
        #Search prices and product names through HTML
        title   =   soup.find("h1", class_  =   "ui-pdp-title").get_text().strip()

        moneySymbol =   soup.find("span",   class_  =   "andes-money-amount__currency-symbol").get_text()
        price   =  soup.find("span", class_    =   "andes-money-amount__fraction").get_text().strip()
        dec =   soup.find("span",   class_  =   "andes-money-amount__cents andes-money-amount__cents--superscript-36").get_text().strip()
    
        print("\n Product:")
        print(title)
        print("\n Price:")
        print(moneySymbol, price + "," + dec)
        
    except  AttributeError:
        #If the product price has no decimal places
        print("\n Product:")
        print(title)
        print("\n Price:")
        print(moneySymbol, price)

    
scrap()
