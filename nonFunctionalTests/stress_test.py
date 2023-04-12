import time
import pytest
import requests
baseUrl = 'http://localhost:8800/people/12'
def request_people():
    return requests.get(url=baseUrl)

def test_my_stuff(benchmark):
    response = benchmark(request_people)
    assert response.status_code == 200
