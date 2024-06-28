import pandas as pd
import datetime
date = datetime.date.today().strftime("%#d-%#m-%Y")
print(date)

def Home_joint():

    excel_1 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Sathiya " + date + ".xlsx")
    excel_2 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Vasanth " + date + ".xlsx")
    excel_3 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Darling "+date+".xlsx")
    excel_4 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Viveks " + date + ".xlsx")
    excel_5 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Croma "+date+".xlsx")
    excel_6 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Amazon " + date + ".xlsx")
    excel_7 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Flipkart "+date+".xlsx")
    excel_8 = pd.read_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Total Scraping\Home Application Reliance "+date+".xlsx")



    data = excel_1.merge(excel_2.merge(excel_3.merge(excel_4.merge(excel_5.merge(excel_6.merge(excel_7.merge(excel_8)))))))

    print(data.head())
    print(data.columns)

    test_data = data[["Product Id","Item Code",'Model',"Poorvika", 'Sathiya Price','Vasanth Price','Darling Price',"Vivek's Price","Croma Price","Amazon Price","Flipkart Price","Reliance Price"]]

    test_data.to_excel(r"D:\Durai\Scraping\Home_appliances\Save Date's\Save Files\Home Application All "+date+".xlsx",index=False)

