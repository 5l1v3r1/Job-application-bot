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
rate = 35

client_name = ""

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

login_to_jobs(user_name, password) #ADD TO MAIN

# //*[@id="wyzantResponsiveColumns"]/div[1]/h4

def customized_pitch(client_name):
	pitch = f"Hello {client_name}, how good am I at python programming? Well, this job application was actually made by one of the bots I made using python. "
	pitch += "On a more serious note, I have been a tutor for more than 3 years now and I assisted have multiple students reach their academic goals "
	pitch += "such as this bot for example!"
	return pitch


def apply_to_job(course):
	course = course.title()
	job_link = driver.find_element_by_link_text(course)
	job_link.click()

	# Grabbing the client's first name
	client_name = driver.find_element_by_xpath("//*[@id='wyzantResponsiveColumns']/div[1]/h4").text

	#Add elevator pitch to the appliction
	# pitch = customized_pitch(client_name)
	# pitch_insert = driver.find_element_by_xpath("//*[@id='personal_message']")
	# pitch_insert.clear()
	# pitch_insert.send_keys(pitch)
	
	#negotiate the price
	recomm_hourly_rate = driver.find_element_by_xpath("//*[@id='job_application_form']/div[4]/div[2]/p").text
	recomm_hourly_rate = int(recomm_hourly_rate[2:]) #remove the dollar sign

	# insert higher rate in application
	submit_rate = driver.find_element_by_xpath("//*[@id='hourly_rate']")
	submit_rate.clear()

	# swap regular hourly rate if the recommended rate is high
	if recomm_hourly_rate > rate:
		submit_rate.send_keys(str(recomm_hourly_rate))
	else:
		submit_rate.send_keys(str(rate))

	# submit job application
	button = driver.find_element_by_xpath("//*[@id='job_application_form']/input[5]")
	button.click()

apply_to_job("python")

# driver.close()