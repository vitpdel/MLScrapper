from xml.etree.ElementTree import QName
from    bs4 import  BeautifulSoup
import  requests
from    time    import  sleep

URL =   input("Please, enter the product url: \n >> ")
    
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

        try:
            dec =   soup.find("span",   class_  ="andes-money-amount__cents andes-money-amount__cents--superscript-16").get_text().strip()
        except TypeError:
            dec =   soup.find("span",   class_  =   "andes-money-amount__cents andes-money-amount__cents--superscript-36")

        global  priceF
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
    #Search discounts through HTML
    try:
        discounts   =   soup.find("span",   class_  =   "andes-money-amount__discount").get_text().strip()
        discountsNum    =   int(discounts[0:2])

        priceFNum   =   priceF[3:10]
        print(priceFNum)
        priceFNum1  =   priceFNum.replace(".","")
        print(priceFNum1)
        priceFNum2  =   priceFNum1.replace(",",".")
        print(priceFNum2)

        priceFNumFloat  =   float(priceFNum2)

        discountsPriceF  =   priceFNumFloat  -   (priceFNumFloat*(discountsNum/100))

        #discountsNumDec   =   discountsNum    /   100
        #print(discountsNumDec)
        #discountsPriceF    =   float(priceFNum2)  *   int(discountsNumDec)
        #print(discountsPriceF)

        ##discountsMoneySymbol    =   soup.find("span",   class_  =   "andes-money-amount__currency-symbol")
        ##discountsPrice  =   soup.find("span",   class_  =   "andes-money-amount__fraction")
        ##discountsDec    =   soup.find("sppan",  class_  =   "andes-money-amount__cents andes-money-amount__cents--superscript-36").get_text()  
        ##discountsPriceF =   str(discountsMoneySymbol)    +   " " +   str(discountsPrice)  +   "," + str(discountsDec)


        print("\n Discounts: \n", str(discounts)    +    ":",   float(discountsPriceF))
    except  AttributeError  as  error: 
        print(error)
        discounts   =   "No discounts"
        return  print("\n Discounts: \n",   discounts )


def looping():
    choice  =   input("\n How often do you want to receive product information updates (1, 2, 3...)? \n >> ")
    numChoice   =   int(choice[0:2])

    timeLoop    =   numChoice   *   60  *   60  
    while   True:
        sleep(timeLoop)
        print("\n \n \n PRODUCT INFORMATION UPDATES: \n")
        scrap()


def loopingChoice():
    loopingchoice  =   input("\n Do you wish to receive this information in a loop? [Y/N] \n >> ")

    if  loopingChoice  ==  "Y" or  "Yes"   or  "y" or  "yes":
        looping()
    elif    loopingChoice   ==  "N" or  "No"    or  "n" or  "no":
        return  0
    
scrap()
loopingChoice()