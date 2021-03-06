import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# For #using Chrome , create an instance of Chrome WebDrier
from selenium.webdriver.remote.webelement import WebElement

Browser = webdriver.Chrome("/Users/maveg/OneDrive/Desktop/chromedriver")
# Call Browser.get method too navigate to a page given by the url
Browser.get("https://www.bestbuy.com/site/lego-icons-porsche-911-10295/6434063.p?skuId=6434063")
# Boolean flag to verify each button process
buyButton = False
goButton = False
checkoutButton = False
while not buyButton:
    # Test for blocks of code for errors
    try:
        # WebDriver offers a number of ways to find elements using one of the find_element_by_* methods
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-disabled")
        print("Button isn,t ready yet.")
        # Refresh page after a delay
        time.sleep(1)
        Browser.refresh()
    # Block lets you handle the error (aka solution)
    except:
        addToCartBtn = addButton = Browser.find_element_by_class_name("btn-primary")
        addToCartBtn.click()
        print("Add To Cart Button was Clicked")
        # Needed to not crash and time to search for element
        time.sleep(2)
        buyButton = True
while not goButton:
    try:
        goToCartBtn = goButton = Browser.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a")
        goToCartBtn.click()
        print("Go To Cart Button Complete...")
        # Needed to not crash and time to search for element
        time.sleep(1)
        goButton = True
    except:
        print("Need to run test for failure of clicking the go to cart button ")
while not checkoutButton:
    try:
        checkoutBtn = checkButton = Browser.find_element_by_class_name("btn-lg")
        checkoutBtn.click()
        print("Checkout Button Complete...")
        # Needed to not crash and time to search for element
        time.sleep(1)
        checkoutButton = True
    except:
        print("Need to run test for failure of clicking the checkout Button...")
logIn= False
while not logIn:
    try:
        print("Entering Log in Information.")
        # Locate the ID locator for username and password
        email = Browser.find_element_by_id("fld-e")
        # Send key to the browser
        email.send_keys("Mario.andresvega@yahoo.com")
        time.sleep(1)
        password = Browser.find_element_by_id("fld-p1")
        password.send_keys("Killersavage123")
        login = Browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button")
        login.click()
        logIn = True
    except:
        print("Need to run test... For failure of loging in.")
print("Up to Date")



