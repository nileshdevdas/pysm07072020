from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://hrms.vinsys.com/Login")
username_field = driver.find_element_by_name("user")
username_field.send_keys("nilesh.devdas@vinsys.com")
password_field = driver.find_element_by_name("password")
password_field.send_keys("somepassword")

#driver.close()

