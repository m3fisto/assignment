This is a POC project with Python for testing a fake API server both for functional testing and non-functional testing
## Installation

# install python 3

```sh
brew install python
```

# install pip

https://phoenixnap.com/kb/install-pip-mac


# install flask
```sh
pip install flask
```
# install robot
pip install robotframework-seleniumlibrary

# install flask
pip freeze > requirements.txt

# install requests
pip install requests


# create the docker image
docker build -t flask-rest-api .


#  run the docker container locally
docker run -d -p 5000:5000 flask-rest-api



#  run performance tests
k6 run -u 10 -d 60s ./nonFunctionalTests/performance-test.js


pip install jsonpath-ng