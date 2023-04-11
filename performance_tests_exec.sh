#!/bin/bash
echo "Running service..."
docker run -d --name api-sw -p 8800:8800 api-sw
sleep 1
echo "Service Started. Starting performance tests..."
k6 run -u 10 -d 60s ./nonFunctionalTests/performance-test.js
echo "Completed performance tests. Stopping  service.."
docker stop api-sw
docker rm api-sw
echo "Service stopped"
