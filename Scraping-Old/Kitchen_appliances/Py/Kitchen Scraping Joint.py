import pandas as pd
import datetime
date = datetime.date.today().strftime("%#d-%#m-%Y")
print(date)


excel_1 = pd.read_excel(r"D:\Durai\Scraping\Kitchen_appliances\Save Data\Scraping Data\Total Scraping\KA Price Lists 1 Price List " + date + ".xlsx")
excel_2 = pd.read_excel(r"D:\Durai\Scraping\Kitchen_appliances\Save Data\Scraping Data\Total Scraping\KA Price Lists 2 Price List " + date + ".xlsx")
excel_3 = pd.read_excel(r"D:\Durai\Scraping\Kitchen_appliances\Save Data\Scraping Data\Total Scraping\KA Price Lists 3 Price List " + date + ".xlsx")

excel_joint = pd.concat([excel_1,excel_2.dropna(subset='Model Name'),excel_3.dropna(subset='Model Name')])


excel_get_data = excel_joint[['Model Name', 'Poorvika Price', 'Flipkart Price',
                              'Amazon Price', 'Croma Price', 'Vijay Sale Price',
                              'Reliance Digital Price']]

print(excel_get_data.isnull().sum())


excel_get_data.to_excel(r"D:\Durai\Scraping\Kitchen_appliances\Save Data\Scraping Data\Kitchen Appliance " + date +".xlsx",index= False)
