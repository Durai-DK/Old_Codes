from selenium import webdriver
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime

date = datetime.date.today().strftime("%d-%m-%Y")

# wb = Workbook()
# ws = wb.active

s = Service(r"/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = ("https://darlingretail.com/collections/mixie/products/preethi-zodiac-2-0-750-watt-mixer-grinder-with-4-jars-mg235")

driver.get(url)
print(driver.find_element(By.CLASS_NAME, '//*[@id="purchase-5572467753125"]/div/span').text)
    # print(box.text)