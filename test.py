import os
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
driver = os.path.join("/usr/bin","chromedriver")

browser = webdriver.Chrome(executable_path=driver,chrome_options=chrome_options)
browser.get("http://165.227.162.126/")

title = browser.title
print('-------------------------------------------------------------')
print('Currently testing ' + title)
print('-------------------------------------------------------------')

if(title != 'Steven Bucholtz | Full Stack Developer'):
    print('Test Failed: Title does not match "Steven Bucholtz | Full Stack Developer"')
else:
    print('Test Passed: Index Page Found')

browser.get('http://165.227.162.126/verifyuser')
print('Test Passed: Admin Page Accessible')

elem = browser.find_element_by_id('cmdline')
print('Test Passed: Command Line Found')

elem.send_keys('login sbucholtz -p password')
elem.send_keys(Keys.RETURN)
print('Test Passed: Logging In')

assert browser.page_source.find("You have logged in. Welcome Steven.")
print('Test Passed: Login Confirmation Text')
browser.save_screenshot('/root/project3/tests/' + time.strftime("%Y%m%d-%H%M%S") + '.png')

browser.close()