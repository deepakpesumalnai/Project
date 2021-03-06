import lemoncheesecake.api as lcc

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from subdir import Sport


@lcc.tags("web")
@lcc.suite("Child")
class Cricket(Sport):
	
	@lcc.test("Launch")
	def test89(self):
		print("Sample_test1")
