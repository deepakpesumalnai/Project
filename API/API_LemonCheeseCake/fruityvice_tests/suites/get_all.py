# suites/get_all.py

import requests
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

GetFruits = {
    "name": "another_name",
    "description": "A suite with a meaningful description",
    "tags": ["important", "a_second_tag", "a_third_tag"],
    "properties": {"type": "acceptance"},
    "links": [
        ("http://bugtracker.example.com/issues/1234", "TICKET-1234"),
        "http://bugtracker.example.com/issues/1235"
    ]
}
@lcc.disabled()
@lcc.suite("GET all fruityvice fruits")
class GetFruits:

    @lcc.test("Get all fruits")
    def get_all_fruits(self):
        url = 'http://www.fruityvice.com/api/fruit/all'
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))