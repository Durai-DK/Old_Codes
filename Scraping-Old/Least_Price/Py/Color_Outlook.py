import datetime
import win32com.client as client

from Outlook.outlook import Outlook_File

of = Outlook_File()
of.data_find(head="Color_Price")


# def all_seller_outlook():
#     date = datetime.datetime.now().strftime("%d-%m-%Y")
#     print(date)
#
#     Acc = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Accessories " + date + ".xlsx"
#     Lap = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Laptop " + date + ".xlsx"
#     Mob = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Mobiles " + date + ".xlsx"
#     Tv = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Tv " + date + ".xlsx"
#     Kit = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Kitchen Appliance " + date + ".xlsx"
#     Tab= r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Tablets " + date + ".xlsx"
#     Home = r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Home appliances " + date + ".xlsx"
#
#
#     body = """
#     <html>
#         <body>
#             <p>Hi Team,</p>
#             <p>I have attached The Price Comparison with Color.</p>
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
#     message.CC = "karthik@poorvika.in; manikandan.r@poorvika.com; ads1@poorvika.in; ads2@poorvika.in; ads3@poorvika.in; ads8@poorvika.in; ads4@poorvika.in; ads8@poorvika.in;" \
#                  " ads5@poorvika.in; ads6@poorvika.in; ads7@poorvika.in; ads8@poorvika.in; ads9@poorvika.in;"
#     message.Subject = "The Price Comparison with Color  " + date
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
