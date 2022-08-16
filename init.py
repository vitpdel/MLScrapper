from cgitb import html
from    bs4 import  BeautifulSoup
import requests

def start():
    """
    [1] SHOW ALL HTML DATA
    [2] FIND ESPECIFIC DATA
    
    """

    choice  =   input(">")

    if  choice  ==  "1":
        dataCollecting()
    elif    choice  ==  "2":
        Find()

def dataCollecting():
    url =   input("Enter url. Example: http://www.example.com  >")

    data    =   BeautifulSoup(html, "html.parser")

    #Colleting data
    html    =   requests.get(url)
    print(html.text)

    #Formating data
    print(data.prettify())


def Find():
    """
    Find By:

    [1] TAG
    [2] ID
    [3] CLASS
    [4] ALL

    """

    choiceFind  =   input(">")

    if  choiceFind  ==  "1":
        tag =   input("FIND TAG: ")
        findByTag   =   data.find(tag)
        print(findByTag.prettify)

    elif    choiceFind  ==  "2":
        Id  =   input("FIND ID: ")
        findById    =   data.find(id=Id)
        print(findById.prettify)

    elif    choiceFind  ==  "3":
        Class   =   input("FIND CLASS: ")
        findByClass =   data.find(class_=Class)
        print(findByClass.prettify)

    elif    choiceFind  ==  "4":
        findAll =   data.find_all("div")
        print(findAll.prettify)

start()