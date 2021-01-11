from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
import colorama

colorama.init()

item_link = input("Paste Item Link: ")
price_limit = float(input("Set Budget Amount: "))
refresh_interval = int(input("Set Refresh Interval (seconds): "))

store = item_link.split('.')[1]

# "https://www.bestbuy.com/site/dynex-dynex-47-75-full-motion-tv-wall-mount-black/6085403.p?skuId=6085403" testing purposes

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(item_link)

if store == "bestbuy":
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
                if float(price.text[1:]) > price_limit:
                    color = colorama.Fore.YELLOW
                    print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                    print(color + "IN STOCK - Out of Budget", price.text)
                else:
                    print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                    print(color + "IN STOCK", price.text)
                    print(item_link)
            else:
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(colorama.Fore.RED + status.text)
            driver.refresh()
            sleep(refresh_interval)
    except:
        driver.quit()
elif store == "newegg":
    try:
        while True:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ProductBuy")))
            status = element.find_element_by_class_name("btn")
            if status.text == "Add to Cart":
                price = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "product-price")))
                color = colorama.Fore.GREEN
                if float(price.text[1:]) > price_limit:
                    color = colorama.Fore.YELLOW
                    print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                    print(color + "IN STOCK - Out of Budget", price.text)
                else:
                    print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                    print(color + "IN STOCK", price.text)
                    print(item_link)
            else:
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(colorama.Fore.RED + status.text)
            driver.refresh()
            sleep(refresh_interval)
    except:
        driver.quit()
elif store == "amazon":

    while True:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "availability")))
        status = element.find_element_by_class_name("a-color-success")

        if status.text == "In Stock.":
            price = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "price_inside_buybox")))
            color = colorama.Fore.GREEN
            if float(price.text[1:]) > price_limit:
                color = colorama.Fore.YELLOW
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK - Out of Budget", price.text)
            else:
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK", price.text)
                print(item_link)

        elif status.text == "Available from these sellers.":
            button = status.find_element_by_tag_name('a')
            button.click()
            sellers = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "aod-price-1")))
            seller_price = sellers.find_element_by_class_name('a-price-whole')
            seller_price_fraction = sellers.find_element_by_class_name('a-price-fraction')
            color = colorama.Fore.GREEN
            if float(seller_price.text.replace(',', '') + '.' + seller_price_fraction.text) > price_limit:
                color = colorama.Fore.YELLOW
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK - Out of Budget", seller_price.text + '.' + seller_price_fraction.text)
            else:
                print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
                print(color + "IN STOCK - Other Seller", seller_price.text + '.' + seller_price_fraction.text)
                print(item_link)

        else:
            print(colorama.Fore.WHITE + f'[{datetime.now().strftime("%H:%M:%S")}]', end=" ")
            print(colorama.Fore.RED + status.text)
        driver.refresh()
        sleep(refresh_interval)

    driver.quit()

driver.quit()