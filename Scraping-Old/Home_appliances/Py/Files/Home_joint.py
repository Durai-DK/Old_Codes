import pandas as pd
import datetime
date = datetime.datetime.now().strftime("%#d-%#m-%Y")
print(date)

excel_1 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\files\Home Application 1 "+date+".xlsx")
excel_2 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\files\Home Application 2 "+date+".xlsx")
excel_3 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\files\Home Application 3 "+date+".xlsx")

print(excel_1.columns)
excel_joint = pd.concat([excel_1, excel_2.dropna(subset="Product id"), excel_3.dropna(subset="Product id")])

excel_joint.to_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Home Applaince " + date + ".xlsx", index=False)