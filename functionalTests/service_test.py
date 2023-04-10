import requests
import json
# from jsonpath_ng import jsonpath, parse

baseUrl = 'http://localhost:8085'
def test_get_people() :
    path = "/people/12"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    # assert jsonpath.jsonpath(responseJson,'$.data.name')[0] == 'Obi Wan Kenobi'
   # assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2

def test_get_people_error() :
    path = "/people/102"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 404