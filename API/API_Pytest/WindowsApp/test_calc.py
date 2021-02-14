import pytest
from appium import webdriver


class support():
	
	def getresults(driver):
		displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
		displaytext = displaytext.strip("Display is ")
		displaytext = displaytext.rstrip(' ')
		displaytext = displaytext.lstrip(' ')
		return displaytext


@pytest.fixture(scope="module")
def setup_suite():
	print("Start suite")
	desired_cap = {}
	desired_cap["app"] = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
	setup_suite = webdriver.Remote(
		command_executor='http://127.0.0.1:4723',
		desired_capabilities=desired_cap)
	yield setup_suite
	print("after yield")
	if setup_suite != None:
		setup_suite.quit()


def test_firstTest(setup_suite):
	setup_suite.find_element_by_name("Clear").click()
	setup_suite.find_element_by_name("Seven").click()
	assert support.getresults(setup_suite) == '7', "Not Matched"
	setup_suite.find_element_by_name("Clear").click()


def test_addition(setup_suite):
	setup_suite.find_element_by_name("Clear").click()
	setup_suite.find_element_by_name("One").click()
	setup_suite.find_element_by_name("Plus").click()
	setup_suite.find_element_by_name("Seven").click()
	setup_suite.find_element_by_name("Equals").click()
	assert support.getresults(setup_suite) == '8', "Not Matched"


def test_combination(setup_suite):
	setup_suite.find_element_by_name("Seven").click()
	setup_suite.find_element_by_name("Multiply by").click()
	setup_suite.find_element_by_name("Nine").click()
	setup_suite.find_element_by_name("Plus").click()
	setup_suite.find_element_by_name("One").click()
	setup_suite.find_element_by_name("Equals").click()
	setup_suite.find_element_by_name("Divide by").click()
	setup_suite.find_element_by_name("Eight").click()
	setup_suite.find_element_by_name("Equals").click()
	assert support.getresults(setup_suite) == '8', "Not Matched"


def test_division(setup_suite):
	setup_suite.find_element_by_name("Eight").click()
	setup_suite.find_element_by_name("Eight").click()
	setup_suite.find_element_by_name("Divide by").click()
	setup_suite.find_element_by_name("One").click()
	setup_suite.find_element_by_name("One").click()
	setup_suite.find_element_by_name("Equals").click()
	assert support.getresults(setup_suite) == '8', "Not Matched"


def test_multiplication(setup_suite):
	setup_suite.find_element_by_name("Nine").click()
	setup_suite.find_element_by_name("Multiply by").click()
	setup_suite.find_element_by_name("Nine").click()
	setup_suite.find_element_by_name("Equals").click()
	assert support.getresults(setup_suite) == '81', "Not Matched"


def test_subtraction(setup_suite):
	setup_suite.find_element_by_name("Nine").click()
	setup_suite.find_element_by_name("Minus").click()
	setup_suite.find_element_by_name("One").click()
	setup_suite.find_element_by_name("Equals").click()
	assert support.getresults(setup_suite) == '8', "Not Matched"
