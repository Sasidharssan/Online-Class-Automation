import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Google_Chrome = 0
Username = 'XXXXXXXX'
Password = 'XXXX'
subjects=["15EE701", "15ECP18", "15EEC12", "15EEC08", "15EE753", "15EEC17", "15EE702", "Fine-Arts"]
if Google_Chrome == 1:
     chromedriver_path = 'C:\Program Files (x86)\chromedriver.exe'
     browser = webdriver.Chrome(chromedriver_path)
else:
     chromedriver_path = '/usr/bin/chromedriver'
     brave_path = '/usr/bin/brave' # Or location of .exe file of browser in your system
     option = webdriver.ChromeOptions()
     option.binary_location = brave_path
     browser = webdriver.Chrome(executable_path=chromedriver_path, options=option)

browser.get("https://a.impartus.com/login/#/")
username = browser.find_element_by_id("username")
username.send_keys(Username)
password = browser.find_element_by_id("password")
password.send_keys(Password)
password.send_keys(Keys.RETURN)

time.sleep(10)

def autoclass():
    sub = "/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div[%d]/div[1]/div[1]"
    sublist = [browser.find_element_by_xpath(sub%x).text for x in range(1,6)]

    i=len(sublist)-1
    while i >= 0:
        for x in subjects:
            if x in sublist[i]:
                k=i+1
                break
        i=i-1

    join_pre = '/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div[%d]/div[2]/button'
    join= browser.find_element_by_xpath(join_pre%k)
    join.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)
    join_in = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/button[2]')
    join_in.click()

def tryfunc(a, b):
    for x in range(12):
        if int(datetime.datetime.now().strftime("%M")) >= a and int(datetime.datetime.now().strftime("%M")) < b:
            break
        time.sleep(300)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.refresh()
    time.sleep(600)

def execfunc(a,b):
    print("No Classes for now")
    for x in range(12):
        if int(datetime.datetime.now().strftime("%M")) >= a and int(datetime.datetime.now().strftime("%M")) < b:
            break
        time.sleep(300)
    time.sleep(600)

if int(datetime.datetime.now().strftime("%H")) < 13:
    for x in range(4):
        if int(datetime.datetime.now().strftime("%H")) == 13:
            break
        try:
            autoclass()
            tryfunc(50, 55)
        except:
            execfunc(50, 55)
    print('morning classes are over')
    time.sleep(2400)
    for x in range(3):
        if int(datetime.datetime.now().strftime("%H")) == 16 and int(datetime.datetime.now().strftime("%M")) > 30:
            break
        try:
            autoclass()
            tryfunc(30, 35)
        except:
            execfunc(30, 35)
elif int(datetime.datetime.now().strftime("%H")) < 17:
    for x in range(3):
        if int(datetime.datetime.now().strftime("%H")) == 16 and int(datetime.datetime.now().strftime("%M")) > 30:
            break
        try:
            autoclass()
            tryfunc(30, 35)
        except:
            execfunc(30, 35)
else:
    print("No classes now")
browser.close()
