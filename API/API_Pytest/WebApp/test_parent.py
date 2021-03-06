import os
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

driver = None

@pytest.fixture(scope="module")
def setup_suite():
	print("Start suite Parent")
	chrome_driver_path = os.path.dirname(__file__) + r"\chromedriver.exe"
	driver: WebDriver = webdriver.Chrome(chrome_driver_path)
	
def setup_test( test):
	driver.get('https://www.w3.org/')
	counter = 0
	for a in driver.find_elements_by_xpath('.//a'):
		print( f'start{0}', test)
		print(a.get_attribute('href'))
		##print(counter)
	
def teardown_test( test, status):
	print(f'Test case end: {test} and status is {status}')
	
def teardown_suite():
	driver.close()

def test_89(setup_suite):
	print("Sample_test1")
