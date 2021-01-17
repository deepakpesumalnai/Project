# suites/get_by_family.py
import sys

sys.path.insert(1, 'C:/Users/deepak/PycharmProjects/Project/API/API_LemonCheeseCake/fruityvice_tests/Config/')

import json
import requests
import urllib3
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
import configparser
import os.path as osp

PROJECT_DIR = osp.join(osp.dirname(__file__))

@lcc.suite("GET all fruits from a family")
class GetFruitsSpecific:
    def setup_suite(self):
        urllib3.disable_warnings()
        print("Start suite")
    
    def setup_test(self, test):
        config = configparser.ConfigParser()
        print(f'Start TEST{test}')
        try:
            config = json.load(open(osp.join(PROJECT_DIR, "config.json")))
            secret_key = config['DEFAULT']['SECRET_KEY']
            print(f'Secret key is {secret_key}')
        except Exception as e:
            print(f'exception is {str(e)}')
        print(f'Test case start : {test}')

    def teardown_test(self, test, status):
        print()
        print(f'Test case end: {test} and status is {status}')

    def teardown_suite(self):
        urllib3.disable_warnings()
        print("teardown suite")
     #   print(f'value of app file is {app.sample}')
        
    @lcc.test("Get all Rutaceae fruits")
    @lcc.tags("important")
    def get_rutaceae(self):
        family = 'Rutaceae'
        url = ''.join(['http://www.fruityvice.com/api/fruit/family/', family])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))
    
    @lcc.test("Conditionall_disabled")
    def get_rutaceae_disabled(self):
        family = 'Rutaceae'
        url = ''.join(['http://www.fruityvice.com/api/fruit/family/', family])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))
    
    @lcc.test("Get all Bromeliaceae fruits")
    def get_bromeliaceaeg(self):
        family = 'Bromeliaceae'
        url = ''.join(['http://www.fruityvice.com/api/fruit/family/', family])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))