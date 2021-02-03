# suites/get_all.py

import requests
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

GetFruits = {
	"tags": ["parent", "a_second_tag", "a_third_tag"],
	}


@lcc.suite("GET all fruityvice fruits parent")
class GetFruitsParent:
	
	def setup_suite(self):
		print("Start suite Parent")
	
	def setup_test(self, test):
		print(f'Start Parent TEST{test}')
	
	@lcc.test("Get all fruits")
	def get_all_fruits(self):
		url = 'http://www.fruityvice.com/api/fruit/all'
		lcc.log_info('GET %s' % url)
		response = requests.get(url=url, verify=False)
		check_that("response code", response.status_code, equal_to(200))


class car:
	def sample_parent(self):
		print('intest')
