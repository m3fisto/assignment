import requests
from src import data

def request_people():
    return requests.get(url=data.fullUrl)

def test_api_sw(benchmark):
    response = benchmark(request_people)
    assert response.status_code == 200
