import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
driver = webdriver.Chrome(executable_path=chromedriver_path)

data = []

driver.get("https://www.daft.ie/property-for-rent/dublin?showMap=false&sort=publishDateDesc&pageSize=20&from=0")
time.sleep(3)   # some time to load all the elements
driver.find_elements(By.CSS_SELECTOR, ".cc-modal__main .cc-modal__btn")[1].click()  # accept cookies
time.sleep(3)
page = 0
# going through 13 pages
while page < 14:
    time.sleep(2)   # giving some time to load when going to the next page
    page += 1
    # print(page)   DEBUG
    page_results = driver.find_elements(By.CSS_SELECTOR, ".djuMQD")
    # print(len(results))   DEBUG
    for result in page_results:
        link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

        price = ""
        # check if the element exists
        if len(result.find_elements(By.CSS_SELECTOR, ".hiFkJc span")) > 0:
            price = result.find_element(By.CSS_SELECTOR, ".hiFkJc span").text
        print(price)

        address = ""
        # check if the element exists
        if len(result.find_elements(By.CSS_SELECTOR, ".dzihyY")) > 0:
            address = result.find_element(By.CSS_SELECTOR, ".dzihyY").text
        print(address)

        page_data = {
            "link": link,
            "price": price,
            "address": address,
        }
        data.append(page_data)

    # go to the next page
    driver.find_elements(By.CSS_SELECTOR, ".dPixQH span")[-1].click()


# importing data to excel
df = pd.DataFrame(data)
print(df)
df.to_excel("data.xlsx")

