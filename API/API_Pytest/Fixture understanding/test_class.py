import pytest
from appium import webdriver


@pytest.fixture()
def calc():
	print('As initialize')
	desired_cap = {}
	desired_cap["app"] = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
	calc = webdriver.Remote(
		command_executor='http://127.0.0.1:4723',
		desired_capabilities=desired_cap)
	yield calc
	print('After Yield')
	calc.close()
	
def test_1(calc):
	print('in test 1')
