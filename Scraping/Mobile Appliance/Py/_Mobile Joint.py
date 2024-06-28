import pandas as pd
import datetime
date = datetime.date.today().strftime("%d-%m-%Y")
print(date)

excel_1 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Amazon " + date + ".xlsx")
excel_2 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Croma " + date + ".xlsx")
excel_3 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Bajaj " + date + ".xlsx")
excel_4 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Chennai " + date + ".xlsx")
excel_5 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Flipkart " + date + ".xlsx")
excel_6 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Reliance " + date + ".xlsx")
excel_7 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Sangeetha " + date + ".xlsx")
excel_8 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Supreme " + date + ".xlsx")
excel_9 = pd.read_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\Total Scraping\Mobile Vijay " + date + ".xlsx")

data = excel_1.merge(excel_2.merge(excel_3.merge(excel_4.merge(excel_5.merge(excel_6.merge(excel_7.merge(excel_8.merge(excel_9))))))))

print(data.head())
print(data.columns)

test_data = data[
    ["Item Code", "Model", 'Poorvika Price', 'Flipkart Price','Amazon Price', 'Croma Price', "Chennai Price", "Vijay Price",
     "Reliance Price","Sangeetha Price", "Supreme Price", "Bajaj Price"]]

test_data.to_excel(r"D:\Durai\Scraping\Mobile Appliance\Save Data\Scraping Files\\Mobile Appliances All " + date + ".xlsx", index=False)
