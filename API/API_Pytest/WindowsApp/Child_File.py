import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from Parent_File import ParentClass

class ChildClass(ParentClass):
	def ChildMethod(self):
		print("calling parent method")
		self.letprint()
