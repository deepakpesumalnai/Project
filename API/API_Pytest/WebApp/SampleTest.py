
import os
import sys
import pytest


file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from subdir import Sport

class Cricket(Sport):
	
	def test_89(self):
		print("Sample_test1")
