from Form.Form import *


def Scraping_Accessories():

    heading = "Mobile & Accessories"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Mobiles+%26+Accessories+%3E+Mobile+Accessories%60%5D&page="
    ma_range = 1
    ma = Model(heading=heading, url=url, row_num=ma_range)
    ma.product_page_list(head=heading)

########################################################################################################################

    heading = "Computer & Laptop Accessories"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Computers+%26+Tablets+%3E+Computer+%26+Laptop+Accessories%60%5D&page="
    cl_range = ma.product_num()

    cl = Model(heading=heading, url=url, row_num=cl_range)
    cl.product_page_list(head=heading)

########################################################################################################################

    heading = "Tab & Ipad Accessories"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Computers+%26+Tablets+%3E+Tabs+%26+IPad+Accessories%60%5D&page="
    tl_range = cl.product_num()
    # tl_range = 1

    tl = Model(heading=heading, url=url, row_num=tl_range)
    tl.product_page_list(head=heading)

########################################################################################################################

    heading = "TV Accessories"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60TV+%26+Audio+%3E+Tv+Accessories%60%5D"
    t_range = tl.product_num()
    # ta_range = 1

    t = Model(heading=heading, url=url, row_num=t_range)
    t.product_1()

########################################################################################################################

    heading = "Audio Accessories"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60TV+%26+Audio+%3E+Audio+Brands%60%5D&page="
    a_range = t.product_num()
    # ta_range = 1

    a = Model(heading=heading, url=url, row_num=a_range)
    a.product_page_list(head=heading)

    ########################################################################################################################

    heading = "Smart Technology"
    url = "https://www.poorvika.com/s?categories=categories%3A%3D%5B%60Smart+Technology%60%5D&page="
    st_range = a.product_num()
    # st_range = 1

    st = Model(heading=heading, url=url, row_num=st_range)
    st.product_page_list(head=heading)

########################################################################################################################

    heading = "Personal & Health Care"
    url = "https://www.poorvika.com/s?categories=categories%3A%3D%5B%60Personal+%26+Health+Care%60%5D"
    ph_range = st.product_num()
    # ph_range = 1

    ph = Model(heading=heading, url=url, row_num=ph_range)
    ph.product_1()

########################################################################################################################

def Scraping_Tab():

    heading = "Tablets"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Computers+%26+Tablets+%3E+Tabs+%26+IPad%60%5D&page="

    Tab_range = 1

    Tab = Model(heading=heading, url=url, row_num=Tab_range)
    Tab.product_page_list(head=heading)

########################################################################################################################

def Scraping_Laptop():

    heading = "Laptops"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Computers+%26+Tablets+%3E+Laptop+Brands%60%5D&page= "
    lap_range = 1
    lap = Model(heading=heading, url=url, row_num=lap_range)
    lap.product_page_list(head=heading)

########################################################################################################################

def Scraping_Mobile():

    heading = "Mobiles"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60Mobiles+%26+Accessories+%3E+Mobiles%60%5D&page="
    Mob_range = 1
    Mob = Model(heading=heading, url=url, row_num=Mob_range)
    Mob.product_page_list(head=heading)

########################################################################################################################

def Scraping_Tv():

    heading = "Tv"
    url = "https://www.poorvika.com/s?categories=categories.lvl1%3A%3D%5B%60TV+%26+Audio+%3E+Television%60%5D&stock_status=stock_status%3A%3D%5B%60In+Stock%60%5D&page="
    Tv_range = 1
    Tv = Model(heading=heading, url=url, row_num=Tv_range)
    Tv.product_page_list(head=heading)

########################################################################################################################

def Scraping_Kitchen_Appliances():

    heading = "Kitchen Appliances"
    url = "https://www.poorvika.com/s?categories=categories%3A%3D%5B%60Kitchen+Appliances%60%5D&page="
    KA_range = 1
    KA = Model(heading=heading, url=url, row_num=KA_range)
    KA.product_page_list(head=heading)

########################################################################################################################