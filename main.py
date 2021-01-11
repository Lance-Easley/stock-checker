from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
import colorama

colorama.init()

price_limit = 559.99
item_link = "https://www.bestbuy.com/site/asus-tuf-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439128.p?skuId=6439128"

# "https://www.bestbuy.com/site/dynex-dynex-47-75-full-motion-tv-wall-mount-black/6085403.p?skuId=6085403" testing purposes

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(item_link)

try:
    while True:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fulfillment-add-to-cart-button")))
        status = element.find_element_by_class_name("btn")
        if status.text == "Add to Cart":
            price_element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "priceView-hero-price")))
            price = price_element.find_element_by_tag_name('span')
            color = colorama.Fore.GREEN
            if float(price.text[1:]) >= price_limit:
                color = colorama.Fore.YELLOW
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK", price.text)
                print(item_link)
            else:
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK", price.text)
                print(item_link)
        else:
            print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
            print(colorama.Fore.RED + status.text)
        driver.refresh()
        sleep(5)
except:
    driver.quit()

driver.quit()