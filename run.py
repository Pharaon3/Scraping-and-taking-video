import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time 
from selenium.webdriver.common.action_chains import ActionChains

# options = Options()
# options.add_argument("start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# it's for creating pdf
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')
# end of creating pdf setting.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

# driver.get('https://meine.postbank.de/iob5/#/login')

# driver.get('https://meine.postbank.de/iob5/#/login')

driver.get('https://student.emeritus.org/courses/4208/modules')

mailPath = '//*[@id="student_email"]'
mailSubmitPath = '/html/body/main/div/div/div/form/input[2]'
passwordPath = '//*[@id="user_password"]'
passwordSubmitPath = '//*[@id="new_user"]/input[4]'
titlePath = '//*[@id="context_module_item_812921"]/div/div[1]/div[1]/span/a'

time.sleep(1)
driver.find_element("xpath", mailPath).send_keys('rajatnathan@icloud.com')
driver.find_element("xpath", mailSubmitPath).click()
time.sleep(1)
driver.find_element("xpath", passwordPath).send_keys('deggu0-hiskaz-cebJed')
driver.find_element("xpath", passwordSubmitPath).click()
time.sleep(50)

title = driver.find_element("xpath", titlePath).click()
time.sleep(50)
driver.execute_script('window.print();')
# title = driver.find_element("xpath", titlePath).get_attribute('innerHTML')
print(title)
# driver.find_element("xpath", passwordButtonPath).send_keys(u'\ue007')
# driver.find_element("xpath", passwordPath).send_keys(password)