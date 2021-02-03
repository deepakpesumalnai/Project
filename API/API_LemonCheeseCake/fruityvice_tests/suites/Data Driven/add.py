import os.path as osp
import json
import time
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

PROJECT_DIR = osp.join(osp.dirname(__file__))
starttime = time.perf_counter()


class TestAdd(object):
    def __init__(self, i, j, expected):
        self.i = i
        self.j = j
        self.expected = expected

    def __call__(self):
        endtime = time.perf_counter()
        print(f'Start time is {starttime}')
        print(f'End time is {endtime}')
        print(f'Time difference is {endtime - starttime}')
        check_that(
            "%d + %d" % (self.i, self.j), self.i + self.j, equal_to(self.expected)
        )


@lcc.tags("Only")
@lcc.suite("Add")
class add(object):
    def __init__(self):
        # print("file name")
        # print(PROJECT_DIR)
        # print(__file__)
        data = json.load(open(osp.join(PROJECT_DIR, "data.json")))
        counter = 0
        for entry in data:
            counter = counter + 1
            testname = f'Test case number {counter}'
            test = lcc.Test(
                testname, testname,
                TestAdd(entry["i"], entry["j"], entry["expected"])
            )
            lcc.add_test_into_suite(test, self)