import requests
import pandas as pd
from Py.Form.links import *


class GoogleReviewAndRating:
    def __init__(self):
        self.full_data = []

    def get_request(self, name, title):
        f = open(cred[0]["txt_credentials"], "r")
        acc_file = f.readline()
        f.close

        response = requests.get(url=cred[1]["reviews_url"].format(cred[1]["account_id"], name),
                                headers=cred_header(token=acc_file))
        # print("response : ", response)

        if response.status_code == 200:
            json_response = response.json()
            review = json_response.get('totalReviewCount', [])
            rating = json_response.get('averageRating', [])

            if review == [] or review == '' or review is None:
                review = 0
            else:
                review = int(review)

            if rating == [] or rating == '' or rating is None:
                rating = 0

            else:
                rating = round(rating, 2)

            data = {"Store": title[17:], "Review": review, "Rating": rating}
            print("Data  : ", data)
            self.full_data.append(data)
            # self.data = {}
            print(" ")

        else:
            print({f"error: {response.status_code}, {response.text}"})

    def get_rating(self, start):
        print(" ")
        print("-" * 120)
        print(" ")

        df = pd.read_excel(cred[2]["location_save"])
        end = len(df)
        print("Overall Store's : ", end)
        print(" ")

        for r in range(start, end):
            location = df.iloc[r]
            print("Range : ", r)
            self.get_request(title=location['title'], name=location["name"])
            pd.DataFrame(self.full_data).to_excel(cred[1]["reviews_save"], index=False)


GMB_RR = GoogleReviewAndRating()
