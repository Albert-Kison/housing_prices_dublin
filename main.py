import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from geopy.geocoders import GoogleV3

chromedriver_path = "/Users/albertkison/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_path)

data = []

driver.get("https://www.daft.ie/property-for-rent/dublin?showMap=false&sort=publishDateDesc&pageSize=20&from=0")
time.sleep(3)
driver.find_elements(By.CSS_SELECTOR, ".cc-modal__main .cc-modal__btn")[1].click()
time.sleep(3)
page = 0
while page < 14:
    time.sleep(2)
    page += 1
    print(page)
    results = driver.find_elements(By.CSS_SELECTOR, ".djuMQD")
    print(len(results))
    for result in results:
        link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(link)
        price = ""
        if len(result.find_elements(By.CSS_SELECTOR, ".hiFkJc span")) > 0:
            price = result.find_element(By.CSS_SELECTOR, ".hiFkJc span").text
        print(price)
        address = ""
        if len(result.find_elements(By.CSS_SELECTOR, ".dzihyY")) > 0:
            address = result.find_element(By.CSS_SELECTOR, ".dzihyY").text
        print(address)
        object = {
            "link": link,
            "price": price,
            "address": address,
        }
        data.append(object)
    driver.find_elements(By.CSS_SELECTOR, ".dPixQH span")[-1].click()
# for i in range(0, 4):
#     print("rogjrg")
#     time.sleep(5)
#     if len(driver.find_elements(By.CSS_SELECTOR, "#mh-modal-body .MhIcon")) > 0:
#         driver.find_element(By.CSS_SELECTOR, "#mh-modal-body .MhIcon").click()
#     results = driver.find_elements(By.CSS_SELECTOR, ".PropertyListingCard")
#     print(len(results))
#     for result in results:
#         link = result.find_element(By.CSS_SELECTOR, ".PropertyListingCard__ImageContainer a").get_attribute("href")
#         print(link)
#         price = result.find_element(By.CSS_SELECTOR, ".PropertyListingCard__Price div").text
#         print(price)
#         address = result.find_element(By.CSS_SELECTOR, ".PropertyListingCard__Address").text
#         print(address)
#         object = {
#             "link": link,
#             "price": price,
#             "address": address,
#         }
#         data.append(object)
#     time.sleep(3)
#     if i < 3:
#         driver.find_element(By.CSS_SELECTOR, ".ngx-pagination .pagination-next").click()
#
# print(len(data))
df = pd.DataFrame(data)
print(df)
df.to_excel("data.xlsx")

