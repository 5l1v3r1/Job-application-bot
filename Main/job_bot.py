from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Enter your credentials here
user_name = "michael.luma" #ENTER USER NAME HERE
password = "Y2xUPE84zgWJ%RR" #ENTER PASSWORD HERE


# Path to execute chrome browser from
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
link_login = "https://www.wyzant.com/tutor/jobs"

# Jump straight to website's link
driver.get(link_login)

def login_to_jobs(user_name, password):
	"""
	Logs in the account's jobs page, provided user enters creditials
	user_name: Firstname.Lastname
	password: Your password

	"""
	username_input = driver.find_elements_by_xpath("//*[@id='Username']")[1] #picks the user name input tag
	username_input.send_keys(user_name)

	password_input = driver.find_elements_by_xpath("//*[@id='Password']")[3] #picks the password input tag
	password_input.send_keys(password)

	button = driver.find_elements_by_tag_name("button")[10] #button to login (10th button tag)
	button.click()
	driver.implicitly_wait(5); #wait for a bit, the program is too fast

login_to_jobs(user_name, password)


job_link = driver.find_element_by_link_text("Python")
job_link.click()


# driver.close()