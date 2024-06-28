from google_auth_oauthlib.flow import InstalledAppFlow
from Py.Form.links import *


def access_token():
    print(" ")
    flow = InstalledAppFlow.from_client_secrets_file(cred[0]["client_id"],
                                                     scopes=cred[0]["scope"],
                                                     redirect_uri=cred[0]["redirect_uri"]
                                                     )
    credentials = flow.run_local_server()

    f = open(cred[0]["txt_credentials"], "a")
    f.write(credentials.token)
    f.close()

    print(" ")
    print("-" * 100)
    print(" ")
