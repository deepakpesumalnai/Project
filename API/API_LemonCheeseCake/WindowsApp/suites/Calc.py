from lemoncheesecake.matching import *
from lemoncheesecake.session import *
import lemoncheesecake.api as lcc

from appium import webdriver


@lcc.tags('Calc')
@lcc.suite("Calculator Suite")
class Calculator_class:
	driver = None
	
	def setup_suite(self):
		print("Start suite")
		desired_cap = {}
		desired_cap["app"] = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
		self.driver = webdriver.Remote(
			command_executor='http://127.0.0.1:4723',
			desired_capabilities=desired_cap)
	
	def getresults(self):
		displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
		log_info(displaytext)
		displaytext = displaytext.strip("Display is ")
		displaytext = displaytext.rstrip(' ')
		displaytext = displaytext.lstrip(' ')
		return displaytext
	
	@lcc.tags('sample')
	@lcc.test('SimpletTest')
	def FirstTest(self):
		self.driver.find_element_by_name("Clear").click()
		self.driver.find_element_by_name("Seven").click()
		check_that("value", self.getresults(), equal_to('7'))
		self.driver.find_element_by_name("Clear").click()
	
	@lcc.test('Addition')
	def test_addition(self):
		self.driver.find_element_by_name("One").click()
		self.driver.find_element_by_name("Plus").click()
		self.driver.find_element_by_name("Seven").click()
		self.driver.find_element_by_name("Equals").click()
		check_that("value", self.getresults(), equal_to('8'))
	
	@lcc.test('Mixed')
	def test_combination(self):
		self.driver.find_element_by_name("Seven").click()
		self.driver.find_element_by_name("Multiply by").click()
		self.driver.find_element_by_name("Nine").click()
		self.driver.find_element_by_name("Plus").click()
		self.driver.find_element_by_name("One").click()
		self.driver.find_element_by_name("Equals").click()
		self.driver.find_element_by_name("Divide by").click()
		self.driver.find_element_by_name("Eight").click()
		self.driver.find_element_by_name("Equals").click()
		check_that("value", self.getresults(), equal_to('8'))
	
	@lcc.test('Division')
	def test_division(self):
		self.driver.find_element_by_name("Eight").click()
		self.driver.find_element_by_name("Eight").click()
		self.driver.find_element_by_name("Divide by").click()
		self.driver.find_element_by_name("One").click()
		self.driver.find_element_by_name("One").click()
		self.driver.find_element_by_name("Equals").click()
		check_that("value", self.getresults(), equal_to('8'))
	
	@lcc.test('Multiplication')
	def test_multiplication(self):
		self.driver.find_element_by_name("Nine").click()
		self.driver.find_element_by_name("Multiply by").click()
		self.driver.find_element_by_name("Nine").click()
		self.driver.find_element_by_name("Equals").click()
		check_that("value", self.getresults(), equal_to('81'))
	
	@lcc.test('Subraction')
	def test_subtraction(self):
		self.driver.find_element_by_name("Nine").click()
		self.driver.find_element_by_name("Minus").click()
		self.driver.find_element_by_name("One").click()
		self.driver.find_element_by_name("Equals").click()
		check_that("value", self.getresults(), equal_to('8'))
	
	def teardown_suite(self):
		self.driver.quit()
		print("End suite")
