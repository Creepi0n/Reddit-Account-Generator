from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import re
import string
import secrets
import os
from selenium.webdriver.chrome.options import Options
tor_proxy = "127.0.0.1:9150"

chrome_options = Options()

'''chrome_options.add_argument("--test-type")'''
chrome_options.add_argument('--ignore-certificate-errors')
'''chrome_options.add_argument('--disable-extensions')'''
chrome_options.add_argument('disable-infobars')
'''chrome_options.add_argument("--incognito")'''
chrome_options.add_argument('--user-data=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
chrome_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# GENERATE PASSWORD
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
# PASSWORD GENERATION FINISHED

# NAME GENERATION
driver.get('https://en.wikipedia.org/wiki/Special:Random')
temp = driver.find_element(By.CLASS_NAME, "firstHeading").text
for char in string.punctuation:
    temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, '') #REMOVES SPACES
temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
name = ''.join(temp.split())
name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000,99999)

dirname = os.path.dirname(__file__)
text_file_path = os.path.join(dirname, 'namesforreddit.txt')
text_file = open(text_file_path, "a")
text_file.write('{"username": "'+ name + str(randomNumber) +'","password": "' +password+'"},') #OUTPUTS NAME AND NUMBER
text_file.write("\n")
text_file.close()

finalName = name+str(randomNumber)
time.sleep(1)
# NAME GENERATION FINISHED

# REDDIT ACCOUNT CREATION
driver.get('https://www.reddit.com/register/')
driver.find_element(By.ID, 'regEmail').send_keys('mail@mail.mail')
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()
time.sleep(3)
driver.find_element(By.ID, 'regUsername').send_keys(finalName)
driver.find_element(By.ID, 'regPassword').send_keys(password)

exit()
#So the Script will end and you can restart it.
# driver.close()
