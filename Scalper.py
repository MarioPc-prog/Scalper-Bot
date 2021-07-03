import time
from selenium import webdriver

#For using Chrome , create an instance of Chrome WebDrier
Browser = webdriver.Chrome("/Users/maveg/OneDrive/Desktop/chromedriver")

#Call Browser.get method so you can navigate to a page given by the url .
Browser.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")

print("Test")
