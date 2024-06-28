import datetime
import pandas as pd

date = datetime.date.today().strftime("%d-%m-%Y")
acc_data = pd.read_excel(r"E:\Durai\Scraping\Tv\Save Data's\Scraping Files\Total Scraping\Tv Scraping All " + date + ".xlsx")

data = pd.DataFrame(acc_data)
print(data.columns)

all_price = pd.DataFrame(data[["Item Code", "Model Name", "Poorvika Price", "Flipkart Price", "Amazon Price",
                              "Croma Price", "Vijay Sale Price", "Reliance Digital Price"]])

print(all_price)
all_price.to_excel(r"E:\Durai\Scraping\Tv\Save Data's\Scraping Files\Tv " + date + ".xlsx", index=False)