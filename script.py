from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import os
import sys
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

mearsk_url="https://www.maersk.com/tracking/#tracking/"
tracking_num = "206721128"
def create_folder():
	# directory = os.getcwd()+'\\'+keyword
    PATH= 'C:\\Webdriver\\bin\\chromedriver_win32_v88\\chromedriver.exe'
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    return(PATH)

directory=create_folder()

with webdriver.Chrome(executable_path=directory) as chromedriver:

    try:
    
        # chromedriver = None

        # chromedriver = webdriver.Chrome(directory)
        wait = WebDriverWait(chromedriver, 10)
        # chromedriver.get("https://google.com/ncr")
        if 'browserVersion' in chromedriver.capabilities:
            print(chromedriver.capabilities['browserVersion'])
        else:
            print(chromedriver.capabilities['version'])

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
            # print(first_result.get_attribute("textContent"))
            print("seema")
            print(first_result.text)
        except:
            print("couldnt get package number")


        try:
            # to open up the table dropdown click automatically
            try:
                time.sleep(2)
                chromedriver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[6]/a').click()
                print("dropdown expanded")
            except:
                print("couldnt expand dropdown")

            try:
                # use xpath to get number of rows and columns
                # row = chromedriver.find_elements_by_xpath('//*[@id="table_id"]/tbody/tr/td/span')
                # table_xpath = chromedriver.find_elements_by_xpath('//*[@id="timelineId"]/div[1]/table/tbody/tr')
                # for i in row:
                #     print(row[0].text)
                # print(table_xpath.text)
                # locations = chromedriver.find_elements_by_class_name('timeline__event-table__cell--heading') works
                # locations = chromedriver.find_elements_by_tag_name('tbody') 
                # print(len(locations))

                # timeline__event-table__cell timeline__event-table__cell--heading
                # timeline__event-table__cell timeline__event-table__cell--heading
                # all_rows = chromedriver.find_elements_by_class_name('timeline__event-table__row') works
                all_tables = chromedriver.find_elements_by_class_name('table__wrapper')
                locations = chromedriver.find_elements_by_class_name('timeline__event-table__cell--heading') 
                print(len(all_tables))
                # second_row = chromedriver.find_elements_by_xpath('//*[@id="timelineId"]')
                # print(second_row[0].text)
                # print(len(all_rows))  
                # print(len(all_rows))
                for i in all_tables:
                    # print(i+"th loop")
                    print("--------------start---------")
                    location = i.find_elements_by_class_name('timeline__event-table__cell--heading')
                    print(location.gettext)
                    print('----------stop------------')
                    # print(i[0].text)
                    # dates = chromedriver.find_elements_by_xpath('//*[@id="table_id"]/tbody/tr/td/span')
                    # dates = all_rows.find_elements_by_class_name('timeline__event-table__cell--time')
                    # print(dates.text)
                    # for j in dates:
                    #     print(j)
                # for elem in range(table_xpath):
                #     print("for loop")
            except:
                print("couldnt get table")
            table_xpath = chromedriver.find_element_by_xpath('//*[@id="timelineId"]/div[1]/table/tbody/')
            for elem in range(table_xpath):
                print("for loop")
            table_id = chromedriver.find_element(By.ID, 'table_id')
            rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
            for row in rows:
                # Get the columns (all the column 2)        
                col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
                print(col.text) #prints text from the element
            # second_result = wait.until(presence_of_element_located((By.)))
            print("")
        except:
            print(sys.exec_info())

        # time.sleep(5)
        # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
        # print(first_result.get_attribute("textContent"))

        # print(search.text)
    except:
        chromedriver.quit()


#This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Firefox() as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#     print(first_result.get_attribute("textContent"))