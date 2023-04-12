## This is a POC project with Python for testing a fake API server both for functional testing and non-functional testing
# HOW TO USE


## install python 3
## install docker

# install python dependencies
```sh
•	pip install pytest requests pytest-docker pytest-benchmark pytest-html
```



# create the docker image
```sh
docker build -t api-sw .
```
# start docker container
```sh
docker run -d --name api-sw -p 8800:8800 api-sw

You can reach the service on your local browser on : 
* localhost:8800/people/-number-   
* localhost:8800/planets/-number-   
* localhost:8800/starships/-number-   

```
#  run performance tests
```sh
pytest ./Tests/stress_test.py --html=reportNFT.html --benchmark-min-rounds=50 
```
An html report of the performance tests is generated in reportNFT.html
# run functional tests
```sh
pytest ./Tests/service_test.py --html=reportFT.html
```
An html report of the functional tests is generated in reportFT.html
Server logs are stored in server_app.log file


# run everything without starting manual the service
```sh
pytest --html=report.html  --benchmark-min-rounds=50  
```