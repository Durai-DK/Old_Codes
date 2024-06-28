
def outlook_body(**kwargs):
    Body = """
       <html>
            <body>
                <p>Hi Team,</p>
                <p>I have attached The {} here.</p>
            
                <p>Thanks & Regards,<br>
                    Duraikannan.R<br>
                    Phone: 8682997570</p>
                <p><img src = "D:\Durai\Scraping\Form\Poorvika_logo.png"><br>
                    Poorvika Mobiles Pvt Ltd.</p>
            </body>
        </html>
    """.format(kwargs.get("body"))
    return Body

Data = {
    "GMD": {"TO": "ganapathy.k@poorvika.com; gowrisankar.p@poorvika.com",
            "CC": "hepzi@poorvika.com",
            "Subject": "Google Ratings & Reviews ",
            "att1": r"D:\Durai\Scraping\Reviews_count\Save Fiels\Google Ratings & Reviews ",
            "att_file_len": 1,
            },

    "Flipkart": {"TO": "Rvk@poorvika.com",
                 "CC": 'karthik@poorvika.in; saravanavelu0482@poorvika.com; karpagam0064@poorvika.com; yasararafath1147@poorvika.com; manikandan.r@poorvika.com ',
                 "Subject": "Flipkart All Seller Price  ",
                 "att1": r"D:\Durai\Scraping\Flipkart_3_Hours\Save Data\Flipkart_All_Sellers ",
                 "att_file_len": 1,
                 },

    "Least_Price": {"TO": "thilakkumar0251@poorvika.com",
                    "CC": "karthik@poorvika.in",
                    "Subject": "Least Price list Comparison ",
                    "att1": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Accessories Price List ",
                    "att2": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Laptop Price Lists ",
                    "att3": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Mobiles_Price_List ",
                    "att4": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Tv Price List ",
                    "att5": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Kitchen Appliance ",
                    "att6": r"D:\Durai\Scraping\Least_Price\Save Data\Least Price Tablets ",
                    "att7": r"D:\Durai\Scraping\Least_Price\Save Data\Least Home appliances ",
                    # "att_file_len": 6,
                    "att_file_len": 7,
                    },

    "Color_Price": {"TO": "thilakkumar0251@poorvika.com",
                    "CC": "karthik@poorvika.in; manikandan.r@poorvika.com; ads1@poorvika.in; ads2@poorvika.in; ads3@poorvika.in; ads8@poorvika.in; ads4@poorvika.in; ads8@poorvika.in;" \
                           " ads5@poorvika.in; ads6@poorvika.in; ads7@poorvika.in; ads8@poorvika.in; ads9@poorvika.in; ads10@poorvika.in;",
                    "Subject": "Price Comparison with Color ",
                    "att1": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Accessories ",
                    "att2": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Laptop ",
                    "att3": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Mobiles ",
                    "att4": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Tv ",
                    "att5": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Kitchen Appliance ",
                    "att6": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Tablets ",
                    "att7": r"D:\Durai\Scraping\Least_Price\total_save\Price Comparison Home appliances ",
                    # "att_file_len": 6,
                    "att_file_len": 7,
                    },

}