import pandas
import pytest
import requests
import xml.etree.ElementTree as ET


@pytest.fixture
def wallet():
	print('In fixture     ----------')


def test_default_initial_amount(wallet):
	headers = {'content-type': 'application/soap+xml'}
	url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso'
	body = '''<?xml version="1.0" encoding="utf-8"?>
			<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
            <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
            <ubiNum>500</ubiNum>
            </NumberToWords>
            </soap:Body>
			</soap:Envelope>
			'''
	response = requests.post(url, data=body, headers=headers)
	assert response.status_code == 200
	
	print('status     ----------')
	print(response.status_code)
	print('content     ----------')
	
	print(response.content)
	content = response.content
	with open('topnewsfeed.xml', 'wb') as f:
		f.write(response.content)
	tree = ET.parse('topnewsfeed.xml')
	df = pandas.DataFrame(list(iter_employees(etree)))
	print(df)

def iter_employees(xml_etree):
	# this selects elements in the xml until we get to the return node
	# which contains the items, then we iterate over the items
	for each in xml_etree[0][0][0].iter('item'):
		# for each item, we add to a dictionary the tag and text as a key:value pair
		# while iterating over all tags present
		my_dict = {}
		for info in list(each):
			my_dict[info.tag] = info.text
		# yielding the dictionary allows this function to provide a list of dictionaries
		yield my_dict
