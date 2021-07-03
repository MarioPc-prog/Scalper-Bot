import time
from selenium import webdriver

#For using Chrome , create an instance of Chrome WebDrier
Browser = webdriver.Chrome("/Users/maveg/OneDrive/Desktop/chromedriver")

#Call Browser.get method so you can navigate to a page given by the url .
Browser.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")


#Boolean flag
buyButton = False

while not buyButton:
    try:
        #WebDriver offers a number of ways to find elements using one of the find_element_by_* methods
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-primary")
        print("Test in try")
    except:
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-primary")
        print("Test in except")

