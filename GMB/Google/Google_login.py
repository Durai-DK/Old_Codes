from selenium import webdriver
import hmac,base64,struct,hashlib,time
from selenium.webdriver.common.by import By



url = "https://www.google.com/"
user_name = "dev@poorvika.in"
password = "Prdev@1855"
secret='biyaupm6752z6pzyoiv3vvxhtm3m6hvb'

class Google:
    def __init__(self, driver):
        self.driver = driver

    def next_button(self):
        for next_username in self.driver.find_elements(By.CLASS_NAME, "VfPpkd-vQzf8d"):
            if next_username.text == "Next":
                # print(next_username.text)
                next_username.click()
                break
        self.driver.implicitly_wait(3)

    def username(self):
        self.driver.find_element(By.TAG_NAME, "input").send_keys(user_name)
        Google.next_button(self)


    def user_pass(self):

        self.driver.find_element(By.CLASS_NAME,"whsOnd").send_keys(password)
        Google.next_button(self)


    def get_token(secret,intervals_no = None):
        if intervals_no == None:
            intervals_no = int(time.time()) // 30
        key = base64.b32decode(secret, True)
        msg = struct.pack(">Q", intervals_no)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
        return h

    def Auth(self):
        key=Google.get_token(secret)
        for authkey in self.driver.find_elements(By.CLASS_NAME, "Xb9hP"):
            authkey.find_element(By.TAG_NAME, "input").send_keys(key)
            Google.next_button(self)

    def login(self):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,"gb_Rd").click()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        Google.username(self)
        time.sleep(3)
        Google.user_pass(self)
        time.sleep(3)
        # Google.Authentication(self)
        Google.Auth(self)
        time.sleep(3)
        print("Google My business Login")
        # time.sleep(5)







