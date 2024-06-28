import datetime
import win32com.client as client

from Outlook.outlook import Outlook_File

of = Outlook_File()
of.data_find(head="Flipkart")

# def all_seller_outlook():
#     date = datetime.datetime.now().strftime("%d-%m-%Y")
#     print(date)
#     att_file = r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Flipkart_All_Sellers " + date +".xlsx"
#     print(att_file)
#
#     body = """
#     <html>
#         <body>
#             <p>Hi Team,</p>
#             <p>I have attached The Flipkart All Sellers list here.</p>
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
#     message.To = 'Rvk@poorvika.com'
#     message.CC = 'karthik@poorvika.in; mani2005poorvika@gmail.com; saravanavelu0482@poorvika.com; ' \
#                  'karpagam0064@poorvika.com; yasararafath1147@poorvika.com; manikandan.r@poorvika.com '
#     message.Subject = "Flipkart All Seller Price  " + date
#     message.HTMLBody = body
#     message.Attachments.Add(att_file)
#
#
# all_seller_outlook()
