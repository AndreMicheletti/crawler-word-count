import pytest
import crawler
import requests

@pytest.fixture
def crawler_request(url, word):
	return requests.get("http://localhost:5000?url="+url+"&word="+word)
	
def test_crawler_no_args():
	"""
	GIVEN: a crawler app
	WHEN: GET route "/" without passing anything
	THEN: response code should be 200 and there must be a help message
	"""
	result = requests.get("http://localhost:5000/")
	assert result.status_code == 200
	assert "message" in result.json()
	
	
def test_crawler_empty_args():
	"""
	GIVEN: a crawler app
	WHEN: GET route "/" passing empty arguments
	THEN: response code should be 404 and there must be a message
	"""
	result = crawler_request('','')
	assert result.status_code == 200
	assert "message" in result.json()
	
def test_crawler_invalid_url():
	"""
	GIVEN: a crawler app
	WHEN: GET route "/" passing into URL argument and invalid Website URL
	THEN: response code should be 404
	"""
	result = crawler_request('goo.gle','')
	assert result.status_code == 200
	
def test_crawler_incomplete_url():
	"""
	GIVEN: a crawler app
	WHEN: GET route "/" passing URL argument without http:// in the beggining
	THEN: the URL must be replaced to include http:// in the beggining
	"""
	result = crawler_request('google.com.br','')
	assert 'http://google.com.br' in result.json()
	
def test_crawler_valid_url():
	"""
	GIVEN: a crawler app
	WHEN: GET route "/" passing valid argument
	THEN: response code must be 200 and there must be the result json
	"""
	result = crawler_request('http://google.com.br','google')
	assert result.status_code == 200
	assert 'http://google.com.br' in result.json() 
	assert 'google' in result.text
	