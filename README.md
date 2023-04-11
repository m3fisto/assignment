This is a POC project with Python for testing a fake API server both for functional testing and non-functional testing
## Installation

# install python 3

```sh
brew install python
```

# install pip

https://phoenixnap.com/kb/install-pip-mac


# install pip requirements
```sh
pip install flask requests jsonpath-ng pytest
```


# freeze requirements
```sh
pip freeze > requirements.txt
```


# create the docker image

```sh
docker build -t flask-rest-api .
```

#  run the docker container locally
```sh
docker run -d -p 5001:5001 flask-rest-api
```


#  run performance tests
```sh
k6 run -u 10 -d 60s ./nonFunctionalTests/performance-test.js
```

# run functional tests
```sh
pytest functionalTests
```