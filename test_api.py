import json
import urllib.request

import pytest



@pytest.fixture(scope='module')
def json_api():
	url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
	with urllib.request.urlopen(url) as details_json:
		parsed_contents = json.loads(details_json.read())
		yield parsed_contents


def test_name(json_api):
	"""
	Verify name field contains the text "Carbon credits"
	"""
	name = json_api.get('Name')
	assert name is not None, "Name field not found"
	assert name == 'Carbon credits', "Unexpected text in name field"


def test_can_relist(json_api):
	"""
	Verify CanRelist field contains the boolean "true"
	"""
	can_relist = json_api.get('CanRelist')
	assert can_relist is not None, "CanRelist field not found"
	assert can_relist == True, "Expected CanRelist to be true"


def test_promotions_galley_description(json_api):
	"""
	Verify Promotions element with the name "Gallery" has Description field 
	that contains the text "Good position in category"
	"""
	promotions = json_api.get('Promotions')
	assert promotions is not None, "Promotions field not found"

	gallery_promotion = None
	gallery_description = None
	for promotions_element in promotions:
		if promotions_element.get('Name') == 'Gallery':
			gallery_promotion = promotions_element
			gallery_description = gallery_promotion.get('Description')

	assert gallery_promotion is not None, \
		"Element with name 'Gallery' not found"
	assert gallery_description is not None, \
		"Description field not found in element 'Gallery'"
	assert gallery_description == 'Good position in category', \
		"Unexpected 'Gallery' promotion description"