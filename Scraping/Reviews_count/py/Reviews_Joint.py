import pandas as pd
import datetime
date = datetime.datetime.now().strftime("%d-%m-%Y")
print(date)


excel_1 = pd.read_excel(r"D:\Mohi\Scraping\Reviews_Count\Save Fiels\Scraping Fiels\GMB R&R 1 " + date + ".xlsx")
excel_2 = pd.read_excel(r"D:\Mohi\Scraping\Reviews_Count\Save Fiels\Scraping Fiels\GMB R&R 2 " + date + ".xlsx")
excel_3 = pd.read_excel(r"D:\Mohi\Scraping\Reviews_Count\Save Fiels\Scraping Fiels\GMB R&R 3 " + date + ".xlsx")


print(excel_2.columns)
excel_joint = pd.concat([excel_1,excel_2.dropna(subset='APX'),excel_3.dropna(subset='APX')])

excel_joint.to_excel(r"D:\Mohi\Scraping\Reviews_count\Save Fiels\Google Ratings & Reviews " + date + ".xlsx", index=False)
