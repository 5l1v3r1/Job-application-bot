from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from tutor_secrets import user_name, password, rate, pitches, coursesTaught, jobstoApply


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


def customized_pitch(client_name, course, pitches):
	"""
	Adds the name of the client to the elevator pitch
	client_name: Client's name

	"""
	pitch = pitches[course.title()]
	return pitch.replace("client_name", client_name)


def apply_to_job(coursesTaught, numJobs):

	"""
	Applies to jobs within a certain course
	course: Course to apply jobs for

	"""
	jobsApplied = 0
	while jobsApplied <= numJobs:
		job_link = driver.find_element_by_xpath("//*[@id='jobs-list']/div[1]/div/div/h3/a")
		job_link.click()

		course = driver.find_element_by_xpath("//*[@id='wyzantResponsiveColumns']/div[1]/h1").text.title()

		# Grabbing the client's first name
		client_name = driver.find_element_by_xpath("//*[@id='wyzantResponsiveColumns']/div[1]/h4").text

		# Add elevator pitch to the appliction
		pitch = customized_pitch(client_name, course, pitches)
		pitch_insert = driver.find_element_by_xpath("//*[@id='personal_message']")
		pitch_insert.clear()
		pitch_insert.send_keys(pitch)
		
		#negotiate the price
		try:
			recomm_hourly_rate = driver.find_element_by_xpath("//*[@id='job_application_form']/div[4]/div[2]/p").text
			recomm_hourly_rate = int(recomm_hourly_rate[2:]) #remove the dollar sign
		except:
			recomm_hourly_rate = rate
		# insert higher rate in application
		submit_rate = driver.find_element_by_xpath("//*[@id='hourly_rate']")
		submit_rate.clear()

		# swap regular hourly rate if the recommended rate is high
		if recomm_hourly_rate >= rate:
			submit_rate.send_keys(str(recomm_hourly_rate))
		else:
			submit_rate.send_keys(str(rate))

		# submit job application
		try:
			button = driver.find_element_by_xpath("//*[@id='job_application_form']/input[5]")
			button.click()
			sendText(client_name, recomm_hourly_rate, course)
		jobsApplied += 1

def sendText(client_name, recomm_hourly_rate, course):
	pass

apply_to_job(coursesTaught, jobstoApply)

driver.close()