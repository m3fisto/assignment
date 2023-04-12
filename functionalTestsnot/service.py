import requests
import pytest
# from ..fakeServer import data
baseUrl = 'http://localhost:8800'

def test_get_people() :
    path = "/people/12"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 200
    assert response.json() == [{"name": "Obi Wan Kenobi","sideOfForce":"Light"}]
    # assert response.json() == data.people

def test_get_people_error() :
    path = "/people/102"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 404

def test_get_planet() :
    path = "/planets/12"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 200
    assert response.json() == [{"planet_name": "Dagobah","goesOnVacations": "Darth Vader"}]

def test_get_planet_error() :
    path = "/planets/102"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 404

def test_get_starships() :
    path = "/starships/12"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 200
    assert response.json() == [{"starship_name": "Millennium Falcon","pilot": "Han Solo"}]

def test_get_starships_error() :
    path = "/starships/102"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 404

def test_wrong_format() :
    path = "/people/wrong"
    response = requests.get(url=baseUrl+path)
    assert response.status_code == 404    