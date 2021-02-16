import selenium
from selenium import webdriver as wb
webD = wb.Chrome("C:\\Webdriver\\bin\\chromedriver_win32_v88\\chromedriver.exe")
order_id = "206721128"
webD.get('https://www.maersk.com/tracking/#tracking/'+order_id)

container_tracking = {}

row = webD.find_elements_by_xpath('//*[@id="table_id"]')
col = webD.find_elements_by_xpath('//*[@id="table_id"]/tbody/tr/td/span')
print(len(col))
print(row[0].text,"!!!!")
print(col[0].text,"2222")

for i in range(0,len(col)-3):
    k = 3

    print(col[i+3].text,"yes"+str(i))
    if (col[i+2].text == "Container details"):
        container_tracking[col[i+3].text] = [{'location': col[i+15].text,'events':[{'date_ant_time':col[i+11].text}]
        
        }]
    

print(container_tracking)



    

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