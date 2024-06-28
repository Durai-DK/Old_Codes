from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as service

s = (ChromeDriverManager().install())
driver = webdriver.chrome(ececutable_path="D:\Durai\Driver")


driver.get="https://www.poorvika.com/"
