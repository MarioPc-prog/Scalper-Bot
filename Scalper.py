import time
from selenium import webdriver

#For using Chrome , create an instance of Chrome WebDrier
Browser = webdriver.Chrome("/Users/maveg/OneDrive/Desktop/chromedriver")

#Call Browser.get method so you can navigate to a page given by the url .
Browser.get("https://www.bestbuy.com/site/lego-classic-medium-creative-brick-box-building-set-10696/6252643.p?skuId=6252643&ref=212&loc=1&extStoreId=1502&ref=212&loc=BM01&gclid=CjwKCAjwlYCHBhAQEiwA4K21mwp9SMkEeEfxwyR_S0QyzWU4ZsWnMV57XeN6gKzZT2pG-Y9sf3oAFBoCQrcQAvD_BwE&gclsrc=aw.ds")


#Boolean flag
buyButton = False

while not buyButton:
    try:
        #WebDriver offers a number of ways to find elements using one of the find_element_by_* methods
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-disabled")
        print("Button isn,t ready yet.")
        #Refresh page after a delay
        time.sleep(3)
        Browser.refresh()

    except:
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-primary")
        print("Button was Clicked")
        addToCartBtn.click()
        buyButton = True

