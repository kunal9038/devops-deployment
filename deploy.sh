#!/bin/bash

echo "Pulling latest Docker image..."
docker pull kunalsingh9038/devops-deployment

echo "Stopping old container..."
docker stop devops-container || true
docker rm devops-container || true

echo "Starting new container..."
docker run -d -p 5000:5000 --name devops-container kunalsingh9038/devops-deployment

echo "Deployment completed!"
