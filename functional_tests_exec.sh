#!/bin/bash
echo "Running service..."
docker run -d --name api-sw -p 8800:8800 api-sw
sleep 1
echo "Service Started.  Starting functional tests..."
pytest functionalTests
echo "Completed functional tests. Stopping  service.."
docker stop api-sw
docker rm api-sw
echo "Service stopped"
