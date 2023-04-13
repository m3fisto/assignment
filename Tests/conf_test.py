import pytest
import requests
from requests.exceptions import ConnectionError
from src import data

url = data.fullUrl

def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def api_sw_service(docker_services):
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url

def test_status_container(api_sw_service,docker_services):
    response = requests.get(url)
    assert response.json() == data.people
