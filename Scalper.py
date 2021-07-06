import time
from selenium import webdriver

# For #using Chrome , create an instance of Chrome WebDrier
Browser = webdriver.Chrome("/Users/maveg/OneDrive/Desktop/chromedriver")
# Call Browser.get method too navigate to a page given by the url
Browser.get("https://www.bestbuy.com/site/lego-ninjago-coles-speeder-car-71706/6395543.p?skuId=6395543")
# Boolean flag to verify success and control within the while loop
buyButton = False
while not buyButton:
    # Test for blocks of code for errors
    try:
        # WebDriver offers a number of ways to find elements using one of the find_element_by_* methods
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-disabled")
        print("Button isn,t ready yet.")
        # Refresh page after a delay
        time.sleep(3)
        Browser.refresh()
    # Block lets you handle the error (aka solution)
    except:
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-primary")
        addToCartBtn.click()
        print("Add To Cart Button was Clicked")
        time.sleep(3)
        buyButton = True
print("Test Add To Cart Complete...")
goToCartBtn = goButton = Browser.find_element_by_xpath(
    "/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a")
goToCartBtn.click()
print("Test Go To Cart Complete...")



