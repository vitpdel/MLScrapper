from itertools import product
from    bs4 import  BeautifulSoup
import  requests

URL =   input("Please, enter the product url: ")
    
#This makes scraping work with any browser
headers =   {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}
html  =   requests.get(URL,    headers=headers)
soup    =   BeautifulSoup(html.text, "html.parser")

def scrap():
    try:
        #Search prices and product names through HTML
        title   =   soup.find("h1", class_  =   "ui-pdp-title").get_text().strip()

        moneySymbol =   soup.find("span",   class_  =   "andes-money-amount__currency-symbol").get_text()
        price   =  soup.find("span", class_    =   "andes-money-amount__fraction").get_text().strip()
        dec =   soup.find("span",   class_  =   "andes-money-amount__cents andes-money-amount__cents--superscript-36").get_text().strip()
        
        priceF  =   moneySymbol + " " + price + "," + dec
        
        print("\n Product: \n",    title)
        print("\n Price:    \n",  priceF)

    except  AttributeError:
        #If the product price has no decimal places
        priceFNoDec =   moneySymbol +   " " + price

        print("\n Product: \n", title)
        print("\n Price: \n", priceFNoDec )
    
    discounts()


def discounts():
    #Search discounts
    try:
        discounts   =   soup.find("span",   class_  =   "andes-money-amount__discount").get_text().strip()
        
        print("\n Discounts: \n", discounts)
    except  AttributeError: 
        discounts   =   "No discounts"
        return  print("\n Discounts: \n",   discounts )
    
scrap()
