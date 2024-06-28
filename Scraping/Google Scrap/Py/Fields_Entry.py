import form
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)

Excel_Sheet_save_location = r"E:\Durai\Scraping\Google Scrap\Save Data's\ "


gm = form.GoogleMaps(Title="villas with swimming pool for monthly rent", Location="Chennai",Save_Excel=Excel_Sheet_save_location)
gm.search_text()
