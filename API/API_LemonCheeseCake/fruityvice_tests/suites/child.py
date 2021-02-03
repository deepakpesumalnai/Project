import sys
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import requests
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
#sys.path.insert(1, 'C:/Users/deepak/PycharmProjects/Project/API/API_LemonCheeseCake/fruityvice_tests/suites/')

from Vehicle import *

GetFruits = {
    "tags": ["Child", "a_second_tag", "a_third_tag"]
}
@lcc.tags("Child")
@lcc.suite("GET all fruityvice fruits child")
class GetFruitsChild(GetFruitsParent):
    #def setup_suite(self):
     #   print("Start suite child")
    
   # def setup_test(self, test):
    #    print(f'Start child TEST{test}')
    
    @lcc.test("Get all fruits")
    def get_all_fruits(self):
        url = 'http://www.fruityvice.com/api/fruit/all'
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))
        print(f'in child Test')


class child_sample(car):
    def child_test(self):
        print('child')