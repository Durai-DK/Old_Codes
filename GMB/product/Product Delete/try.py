from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from GMB.Google.Google_login import Google
import time

url = "https://business.google.com/products/l/02083316379263937574"

driver = webdriver.Chrome(r"D:\Durai\Driver\chromedriver.exe")
g = Google(driver=driver)
g.login()
l = ["Win a Car*, Bike* & More with Poorvika's Feedback Contest!","Free ₹3,999* worth Goodies with Laptops | Deepavali Deals","Groom & Style with Personal Care Gadgets | Upto 35%* off","Upto 70%* Off on Smart Home Devices this Deepavali!","Smart TVs from just ₹9,999*! Grab Free Mi Smart Speaker","Flaunt a Brand New Smartwatch | Upto 75%* Off","Snatch Upto ₹7,000* Benefits on Branded Smartphones!","Get upto ₹6,000* worth Benefits on Tablets & iPads;","Grab Upto 65% Off on TWS Earbuds! Poorvika Deepavali Deals","Upto 70% Off on Wireless Headphones! Celebrate Freedom!"]
