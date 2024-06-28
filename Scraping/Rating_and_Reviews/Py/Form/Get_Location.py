import requests
import pandas as pd
from Py.Form.links import *


class GoogleMYBusiness:
    def __init__(self):
        self.param = cred[2]["params"]
        self.page_token = ""
        self.location_data = []

    def req_list(self):
        self.param["page_token"] = self.page_token
        while self.page_token:
            self.get_location()

    def get_location(self):
        f = open(cred[0]["txt_credentials"], "r")
        acc_file = f.readline()
        f.close

        response = requests.get(url=cred[2]["location_url"].format(cred[1]["account_id"]),
                                headers=cred_header(token=acc_file),
                                params=self.param)
        # print("url : ", cred[2]["location_url"].format(cred[1]["account_id"]))
        # print("headers : ", cred_header(token=acc_file))
        # print("params : ", self.param)
        # print("response : ", response)

        if response.status_code == 200:
            json_response = response.json()
            self.location_data += json_response.get('locations', [])
            print("Location Data Count : ", len(self.location_data))
            self.req_list()
            self.save_excel()

            self.page_token = json_response.get('nextPageToken')

        else:
            print({f"error: {response.status_code}, {response.text}"})

    def save_excel(self):
        df = pd.DataFrame(self.location_data)
        df = df[["title", "name", 'storeCode']]
        df.to_excel(cred[2]["location_save"], index=False)


GMB_Loc = GoogleMYBusiness()
# GMB_Loc.get_location()
