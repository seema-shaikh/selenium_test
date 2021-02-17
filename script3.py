import selenium
from selenium import webdriver as wb
webD = wb.Chrome("C:\\Webdriver\\bin\\chromedriver_win32_v88\\chromedriver.exe")
order_id = "206721128"
webD.get('https://www.maersk.com/tracking/#tracking/'+order_id)

container_tracking = {}


webD.implicitly_wait(20) 

webD.find_element_by_xpath('//*[@id="coiPage-1"]/div[2]/button[2]').click()

row = webD.find_elements_by_xpath('//*[@id="table_id"]')
col = webD.find_elements_by_xpath('//*[@id="table_id"]/tbody/tr/td/span')

webD.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[6]').click()



for i in range(0,len(col)-3):
    k = 3

    print(col[i+3].text,"yes"+str(i))
    if (col[i+2].text == "Container details"):
        container_tracking[col[i+3].text] = ""
    

print(container_tracking)



# second_row = webD.find_elements_by_xpath('//*[@id="timelineId"]')
# print(second_row[0].text)


classname = webD.find_elements_by_class_name('timeline__event-table')
ppp = classname[0]
ppp1 = ppp.find_elements_by_tag_name('td')
pp2 = ppp1[0].get_property('class')

ll = webD.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Location"]')


out=[]

out = []

location_details = webD.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Location"]')
date_and_time_details = webD.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Date and time"]')  
activity = webD.find_elements_by_xpath('//*[@id="timelineId"]/div/table/tbody/tr/td[@data-th="Activity"]')  

for i in range(0,len(location_details)):
    inside = {}
    
    inside['location'] = location_details[i].text
    inside['events'] = [{'date_and_time':date_and_time_details[i].text,'activity':activity[i].text}]
    
    out.append(inside.copy())

print(out,"22222222")

#     print(container_tracking['TGBU8925810'][0]['location'] = "") 

# for el in classname:
    
#     pp2 = pp1.find_elemen


# “container_tracking”: {
# “<CONTAINER_IDs>”: [
# {
# “location”: “<LOCATION>,
# “events”: [{
# “date_and_time”: “<Date and time of the activity eg. 03-Dec-20
# 08:30(format) >”,
# “activity”: “<ACTIVITY>”,
# “status”: “done/pending”
# }, {...}, ...]
# }
# ], ….
# }
print(container_tracking)