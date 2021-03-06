import os
import lemoncheesecake.api as lcc
from selenium import webdriver



@lcc.tags("web")
@lcc.suite("Driver Launch")
class Sport:
	driver = None
	
	def setup_suite(self):
		print("Start suite Parent")
		chrome_driver_path = os.path.dirname(__file__) + r"\chromedriver.exe"
		self.driver = webdriver.Chrome(chrome_driver_path)
	
	def setup_test(self, test):
		self.driver.get('https://www.w3.org/')
		counter = 0
		for a in self.driver.find_elements_by_xpath('.//a'):
			print( f'start{0}', test)
			##print(a.get_attribute('href'))
			##print(counter)
	
	def teardown_test(self, test, status):
		print(f'Test case end: {test} and status is {status}')
	
	def teardown_suite(self):
		self.driver.close()
