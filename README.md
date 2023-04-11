## This is a POC project with Python for testing a fake API server both for functional testing and non-functional testing
# HOW TO USE

# create the docker image

```sh
./create_docker_image.sh
```


#  run performance tests
```sh
./performance_tests.sh
```

# run functional tests
```sh
./functional_tests.sh
```

Server logs are stored in record.log file


# MANUAL INSTALLATION:



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



#  run the docker container locally
```sh
docker run -d -p 5001:5001 flask-rest-api
```


 pip3 install robotframework-requests.