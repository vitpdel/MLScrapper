from xml.etree.ElementTree import QName
from    bs4 import  BeautifulSoup
import  requests
from    time    import  sleep

URL =   input("Please, enter the product url: \n >> ")
    
#This makes scraping work with any browser
headers =   {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}
html  =   requests.get(URL,    headers=headers)
soup    =   BeautifulSoup(html.text, "html.parser")

class   Scrapp:
    def scrap(self):
        try:
            #Search prices and product names through HTML
            title   =   soup.find("h1", class_  =   "ui-pdp-title").get_text().strip()

            moneySymbol =   soup.find("span",   class_  =   "andes-money-amount__currency-symbol").get_text()
            price   =  soup.find("span", class_    =   "andes-money-amount__fraction").get_text().strip()

            try:
                dec =   soup.find("span",   class_  ="andes-money-amount__cents andes-money-amount__cents--superscript-16").get_text().strip()
            except TypeError:
                dec =   soup.find("span",   class_  =   "andes-money-amount__cents andes-money-amount__cents--superscript-36")

            self.priceF  =   moneySymbol + " " + price + "," + dec

            print("\n Product: \n",    title)
            print("\n Price:    \n",  priceF)

        except  AttributeError:
            #If the product price has no decimal places
            priceFNoDec =   moneySymbol +   " " + price

            print("\n Product: \n", title)
            print("\n Price: \n", priceFNoDec )

        self.discounts()


    def discounts(self):
        #Search discounts through HTML
        try:
            discounts   =   soup.find("span",   class_  =   "andes-money-amount__discount").get_text().strip()
            discountsNum    =   int(discounts[0:2])

            priceFNum   =   self.priceF[3:10]
            priceFNum1  =   priceFNum.replace(".","")
            priceFNum2  =   priceFNum1.replace(",",".")

            priceFNumFloat  =   float(priceFNum2)

            discountsPriceF  =   priceFNumFloat  -   (priceFNumFloat*(discountsNum/100))


            print("\n Discounts: \n", str(discounts)    +    ":",   float(discountsPriceF))
        except  AttributeError  as  error: 
            print(error)
            discounts   =   "No discounts"
            return  print("\n Discounts: \n",   discounts )


    def looping(self):

            choice  =   input("\n How often do you want to receive product information updates (1, 2, 3...)? \n >> ")
            numChoice   =   int(choice[0:2])

            timeLoop    =   numChoice   *   60  *   60  
            while   True:
                try:
                    sleep(timeLoop)
                    print("\n \n \n PRODUCT INFORMATION UPDATES: \n")
                    self.scrap()

                except  KeyboardInterrupt:
                    res = input("\n Ctrl-c was pressed. Do you really want to exit? [Y/N] \n >> ")
                    if  res ==  "Y" or  "Yes"   or  "y" or  "yes":
                        break
                    elif    res ==  "N" or  "No"    or  "n" or  "no":
                        continue

    def loopingChoice(self):
        loopingchoice  =   input("\n Do you wish to receive this information in a loop? [Y/N] \n >> ")

        if  loopingchoice  ==  "Y" or  "Yes"   or  "y" or  "yes":
            self.looping()
        elif    loopingchoice   ==  "N" or  "No"    or  "n" or  "no":
            return  0
    
Scrapp.scrap()
Scrapp.loopingChoice()
