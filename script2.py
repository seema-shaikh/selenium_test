from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import os
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import json

import json   
       
# Data to be written   
# dictionary ={   
#   "id": "04",   
#   "name": "sunil",   
#   "depatment": "HR"
# }  


mearsk_url="https://www.maersk.com/tracking/#tracking/"
list_of_tracking_num = ['206721128','206721129','206721130']
tracking_num = "206721128"

inside_dict ={}
dictionary = dict.fromkeys(['container_tracking'])
# dictionary.update(inside_dict)


def create_folder():
    	# directory = os.getcwd()+'\\'+keyword
    PATH= 'C:\\Webdriver\\bin\\chromedriver_win32_v88\\chromedriver.exe'
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    return(PATH)

directory=create_folder()


with webdriver.Chrome(executable_path=directory) as chromedriver:
    wait = WebDriverWait(chromedriver, 10)
    chromedriver.get("https://www.maersk.com/tracking/#tracking/")
    search = chromedriver.find_element_by_id("trackShipmentSearch")
    search.send_keys(tracking_num)
    search.send_keys(Keys.RETURN)

    # to accept cookies automatically
    try:
        chromedriver.find_element_by_xpath('//*[@id="coiPage-1"]/div[2]/button[2]').click()
    except:
        print("cookies not accepted")

    try:

        first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "#table_id > tbody > tr > td.first-element > span:nth-child(4)")))
        print(first_result.text)
        inside_dict=dict.fromkeys([first_result.text])
        dictionary['container_tracking'] = inside_dict  

        chromedriver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[6]/a').click()
        table_id = chromedriver.find_element(By.ID, 'timelineId')
        rows = table_id.find_elements(By.TAG_NAME, 'table')
        for row in rows:
            print('start')
            
            col = row.find_elements(By.TAG_NAME,"tr")
            location = col[0].text        
            # print(col[0].text)
            # print('location')
            # for j in range(1,len(col))
            # if()
            # print(len(col))
            datetimelist = []
            # for j in range(0, len(col)):
            for j in col:
                print(j)
                # print(j[0].text)
                # datetime = row.find_elements(By.CSS_SELECTOR, 'timelineId > div:nth-child(' +(col[j]+1)+') > table > tbody > tr:nth-child(2) > td.timeline__event-table__cell.timeline__event-table__cell--time')
                # print(j.fin)
                datetime = j.find_elements(By.CLASS_NAME, 'timeline__event-table__cell--time')
                activity = j.find_elements(By.CLASS_NAME, 'timeline__event-table__cell--desc')
                print(len(datetime))
                datetimelist=[]
                for k in datetime:
                    print(k.text) 
                print("activity")
                for l in activity:
                    print(l.text) 
                # print(len(activity))
                # datetimelist.append(datetime[0].text)
            # print(datetimelist)
            print('------')
            print(datetimelist)
            print('------')

                # # date_and_time_details = j.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Date and time"]') 
                # activity = j.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Activity"]')  
                # print(type(datetime)) 
                # for k in datetime:
                #     # print(type(k))
                #     print('date')
                #     print(k)
                # print(datetime[].text)  

                # for l in activity:
                #     print('activity')
                #     print(l.text)  

    except ElementClickInterceptedException:
        # Use Javascript to scroll down to bottom of page
        print("entered exception")
        chromedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Serializing json    
json_object = json.dumps(dictionary, indent = 4)   
print(json_object) 
