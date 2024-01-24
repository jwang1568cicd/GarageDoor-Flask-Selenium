#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
# create webdriver object
driver = webdriver.Chrome()
 
# get geeksforgeeks.org
driver.get('http://localhost:5000')
 
# get element 
element = driver.find_element(By.ID, "toggle-color-button")

for x in range(4):
    print('Click the door button ' , x+1 ,' times ; inspect the door.') 
    time.sleep(3)
    # click the element
    element.click()
    time.sleep(5)

driver.close()

