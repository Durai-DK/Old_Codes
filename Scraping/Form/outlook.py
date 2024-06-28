import datetime
import win32com.client as client
from Form.outlook_details import Data, outlook_body

date = datetime.datetime.now().strftime("%d-%m-%Y")

class Outlook_File:

    def data(self,**kwargs):
        outlook = client.Dispatch("Outlook.Application")
        message = outlook.CreateItem(0)
        message.Display()
        message.TO = kwargs.get("to")
        message.CC = kwargs.get("cc")
        message.Subject = kwargs.get("subject") + date
        b = outlook_body(body=kwargs.get("subject"))
        message.HTMLBody = b
        s = "att"
        for r in range(1,kwargs.get("att_len")+1):

            print(Data[kwargs.get("title")][s+str(r)])
            message.Attachments.Add(Data[kwargs.get("title")][s+str(r)] + date + ".xlsx")
            # message.Attachments.Add(Data[kwargs.get("title")][s+str(r)])

    def data_find(self,**kwargs):
        of = Outlook_File()
        if kwargs.get('head') == "GMD":
            of.data(to=Data["GMD"]["TO"], cc=Data["GMD"]["CC"],
                    subject=Data["GMD"]["Subject"],
                    att_len=Data["GMD"]["att_file_len"],
                    title="GMD"
                    )
        elif kwargs.get('head') == "Flipkart":
            of.data(to=Data["Flipkart"]["TO"], cc=Data["Flipkart"]["CC"],
                    subject=Data["Flipkart"]["Subject"],
                    att_len=Data["Flipkart"]["att_file_len"],
                    title="Flipkart"
                    )
        elif kwargs.get('head') == "Least_Price":
            of.data(to=Data["Least_Price"]["TO"], cc=Data["Least_Price"]["CC"],
                    subject=Data["Least_Price"]["Subject"],
                    att_len=Data["Least_Price"]["att_file_len"],
                    title="Least_Price"
                    )
        elif kwargs.get('head') == "Color_Price":
            of.data(to=Data["Color_Price"]["TO"], cc=Data["Color_Price"]["CC"],
                    subject=Data["Color_Price"]["Subject"],
                    att_len=Data["Color_Price"]["att_file_len"],
                    title="Color_Price"
                    )