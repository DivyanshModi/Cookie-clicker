from selenium import webdriver
import time

chrome_driver="/Users/divyansh_modi/Deve. tools/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver)
price_list=[]
all_items=[]
driver.get("http://orteil.dashnet.org/experiments/cookie/")
bigcookie=driver.find_element_by_id("cookie")
av_items=[]
time_start=time.time()
buy_time= time.time() + 5
stop_time=time.time()+60*5
available_upgrades=driver.find_element_by_id("store")

while True:
    bigcookie.click()
    if buy_time<=time.time():

        '''price = driver.find_elements_by_css_selector("#store b")
        for _ in price:
            if _.text !="":
                all_items.append(_)
        unav_items=driver.find_element_by_css_selector("#store .grayed b")
        for _ in all_items:
            if _ not in unav_items:
                av_items.append(_)
        for item_price in av_items:
            text = (item_price.text).split("-")
            if len(text) > 1:
                amount = int(text[1].replace(",", ""))
                price_list.append(amount)
        index_of_purchase=price_list.index(max(price_list))
        av_items[index_of_purchase].click()
'''
        # get all store items
        store_item = driver.find_elements_by_css_selector("#store b")
        all_items = [item for item in store_item if item.text != ""]
        # get unavailable items
        exl_items = driver.find_elements_by_css_selector("#store .grayed b")
        # get available items
        avl_items = [item for item in all_items if item not in exl_items]
        # read cost per item
        cost = [int(item_cost.text.split(" - ")[1]) for item_cost in avl_items]

        # purchase item
        index_of_purchase = cost.index(max(cost))
        avl_items[index_of_purchase].click()

        buy_time+=5
    if time_start>=stop_time:
        break






driver.close()
