import pandas as pd
import datetime
date = datetime.datetime.now().strftime("%d-%m-%Y")
print(date)


excel_1 = pd.read_excel(r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Scraping Sheets\flipkart_Scraping 1 " + date +".xlsx")
excel_2 = pd.read_excel(r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Scraping Sheets\flipkart_Scraping 2 " + date +".xlsx")
excel_3 = pd.read_excel(r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Scraping Sheets\flipkart_Scraping 3 " + date +".xlsx")



print(excel_2.columns)
excel_joint = pd.concat([excel_1,excel_2.dropna(subset='Item Code'),excel_3.dropna(subset='Item Code')])


excel_joint.to_excel(r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Flipkart_All_Sellers " + date +".xlsx",index= False)