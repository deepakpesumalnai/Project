import pytest
from appium import webdriver

@pytest.fixture()
def setup_suite():
	print("Start suite")
	desired_cap = {}
	desired_cap["app"] = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
	setup_suite = webdriver.Remote(
	command_executor='http://127.0.0.1:4723',
	desired_capabilities=desired_cap)
	yield  setup_suite
	print("after yield")
	if setup_suite != None:
		setup_suite.quit()
	
def test_firstTest(setup_suite):
	print("helo")
	setup_suite.find_element_by_name("Clear").click()
	setup_suite.find_element_by_name("Seven").click()
	setup_suite.find_element_by_name("Clear").click()