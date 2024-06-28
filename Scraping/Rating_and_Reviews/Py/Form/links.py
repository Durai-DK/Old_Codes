from Py.Form.core import account_id, reviews_url, locations_url
import datetime

today = datetime.datetime.now().strftime("%d-%m-%Y")


def cred_header(token):

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'}
    return headers


cred = [{
        "scope": ['https://www.googleapis.com/auth/business.manage', "openid"],
        "client_id": r"D:\Madhan\Rating_and_Reviews\Py\Form\client_id.json",
        "redirect_uri": "http://localhost:8080/auth/google/callback",
        "txt_credentials": r"D:\Madhan\Rating_and_Reviews\Files\Credentials\credentials {}.txt".format(today)
        },
        {
        "account_id": account_id,
        "reviews_url": reviews_url,
        "reviews_save": r"D:\Madhan\Rating_and_Reviews\Files\Rating_and_Reviews\Rating_and_Reviews {}.xlsx".format(today)
        },
        {
        "location_url": locations_url,
        "location_save": r"D:\Madhan\Rating_and_Reviews\Files\Location\Location {}.xlsx".format(today),
        "params": {"read_mask": ['title', 'name', 'storeCode']}
        }]
