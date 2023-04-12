import pytest
import requests
import time

from requests.exceptions import ConnectionError
url = "http://127.0.0.1:8800/people/12"

def is_responsive(url):
    try:
        print(url)
        response = requests.get(url)
        print (response.status_code)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):

    # url = "http://127.0.0.1:8800/people/12"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url

def test_status_container(http_service,docker_services):
    time.sleep(5)
    response = requests.get(url)
    print (response.status_code)
    assert response.status_code == 200
