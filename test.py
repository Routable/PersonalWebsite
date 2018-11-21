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

try:
  print('-------------------------------------------------------------')
  print('               STARTING VALIDATION TESTS'                     )
  print('-------------------------------------------------------------')

  browser.get("http://165.227.162.126/")
  title = browser.title

  assert "Steven Bucholtz" in browser.title
  print('Test Passed: Page Title')

  browser.get('http://165.227.162.126/verifyuser')
  print('Test Passed: Admin Page Accessible')

  elem = browser.find_element_by_id('cmdline')
  print('Test Passed: Command Line Found')

  elem.send_keys('login sbucholtz -p password')
  elem.send_keys(Keys.RETURN)
  print('Test Passed: Logging In')

  assert browser.page_source.find("You have logged in. Welcome Steven.")
  print('Test Passed: Login Confirmation Text')

  browser.get('http://165.227.162.126/verifyuser')
  elem = browser.find_element_by_id('cmdline')
  elem.send_keys('login wronguser -p wrongpassword')
  elem.send_keys(Keys.RETURN)
  assert "You have logged in. Welcome Steven." not in browser.page_source
  elem = browser.find_element_by_id('login-failed')
  assert "Login failed." in browser.page_source
  print('Test Passed: Failed Login')

  browser.close()
  print('-------------------------------------------------------------')
  print('TEST SUCCESSFUL')
  print('-------------------------------------------------------------')
except Exception:
  browser.save_screenshot('/root/project3/tests/' + time.strftime("%Y%m%d-%H%M%S") + '.png')
  browser.close()
  print('-------------------------------------------------------------')
  print('       TEST FAILED - SEE SCREENSHOT FOR MORE DETAILS'         )
  print('-------------------------------------------------------------')