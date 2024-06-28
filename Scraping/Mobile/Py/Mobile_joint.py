import pandas as pd
import datetime
date = datetime.date.today().strftime("%d-%m-%Y")
print(date)


excel_1 = pd.read_excel(r"E:\Durai\Scraping\Mobile\Save Data's\Scraping Files\Total Scraping\Mobile 1 Scraping All " + date + ".xlsx")
excel_2 = pd.read_excel(r"E:\Durai\Scraping\Mobile\Save Data's\Scraping Files\Total Scraping\Mobile 2 Scraping All " + date + ".xlsx")
excel_3 = pd.read_excel(r"E:\Durai\Scraping\Mobile\Save Data's\Scraping Files\Total Scraping\Mobile 3 Scraping All " + date + ".xlsx")


excel_joint = pd.concat([excel_1,excel_2.dropna(subset='Model Name'),excel_3.dropna(subset='Model Name')])


excel_get_data = excel_joint[['Item Code','Model Name', 'Poorvika Price', 'Flipkart Price', 'Amazon Price',
                              'Croma Price', 'Vijay Sale Price','Reliance Digital Price']]


print(excel_get_data.isnull().sum())


excel_get_data.to_excel(r"E:\Durai\Scraping\Mobile\Save Data's\Scraping Files\Total Scraping\Mobiles " + date + ".xlsx", index=False)
