# pip install pytest
# pip install pytest-html
# pip install pytest-cov
# pip install pytest-xdist
import pytest 

# i shoould have a file whihc start with test 
# i should have a function that starts with test 
# i can have fixutures which will allow me to run before the tests 
# i can have a test skipped 
# i can have a test being run also  have a report generated for both purpose coverage and report 
# i can have a test also cover the total amount of time taken 
# i can also have different type fixture 


def get_login_test_data():
    open("")

@pytest.fixture
def get_webpage():
    ## dummyt make call to dependecnies 
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.FireFox()
    driver.get("https://hrms.vinsys.com/Login")
    username_field = driver.find_element_by_name("user")
    username_field.send_keys("nilesh.devdas@vinsys.com")
    password_field = driver.find_element_by_name("password")
    password_field.send_keys("somepassword")
    return driver
    

#driver.close()
def test_mypage(get_webpage, get_login_test_data):
    pass

def test_login_with_credentials(get_webpage):
    assert get_webpage.driver  is not None




    
