import datetime
import win32com.client as client

from Outlook.outlook import Outlook_File

of = Outlook_File()
of.data_find(head="Least_Price")



# def all_seller_outlook():
#     date = datetime.datetime.now().strftime("%d-%m-%Y")
#     print(date)
#
#     Acc = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Accessories Price List " + date + ".xlsx"
#     Lap = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Laptop Price Lists " + date + ".xlsx"
#     Mob = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Mobiles_Price_List " + date + ".xlsx"
#     Tv = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Tv Price List " + date + ".xlsx"
#     Kit = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Kitchen Appliance " + date + ".xlsx"
#     Home = r"D:\Durai\Scraping\Least_Price\Save Data\Least Home appliances " + date + ".xlsx"
#     Tab = r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Tablets " + date + ".xlsx"
#
#     body = """
#     <html>
#         <body>
#             <p>Hi Team,</p>
#             <p>I have attached The Least Price List Comparison here.</p>
#             <p>Thanks & Regards,<br>
#                 Duraikannan.R<br>
#                 Phone: 8682997570</p>
#             <p><img src = "D:\Durai\GMB\Reviews_count\Poorvika_logo.png"><br>
#                 Poorvika Mobiles Pvt Ltd.</p>
#         </body>
#     </html>
#     """
#
#     outlook = client.Dispatch("Outlook.Application")
#     message = outlook.CreateItem(0)
#     message.Display()
#     message.To = "thilakkumar0251@poorvika.com"
#     message.CC = "karthik@poorvika.in"
#     message.Subject = "Least Price list Comparison  " + date
#     message.HTMLBody = body
#     message.Attachments.Add(Acc)
#     message.Attachments.Add(Lap)
#     message.Attachments.Add(Mob)
#     message.Attachments.Add(Tv)
#     message.Attachments.Add(Kit)
#     message.Attachments.Add(Home)
#     message.Attachments.Add(Tab)
#
#
# all_seller_outlook()
