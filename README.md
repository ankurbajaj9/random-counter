# Microservices Application

This project demonstrates a microservice-based application deployed using Kubernetes. The application consists of two microservices and a PostgreSQL database.

## Microservices

1. **User Service**: Manages user data.
2. **Random Number Service**: Generates random numbers.

## Prerequisites

- Docker
- Kubernetes
- kubectl
- Helm

## Setup

### 1. Build and Push Docker Images

Navigate to the `backend/docker` directory and build the Docker images for each service:

```sh
# Build and push User Service
cd user_service
docker build -t user_service .
docker push user_service

# Build and push Random Number Service
cd ../random_service
docker build -t random_number_service .
docker push random_number_service

# get bitnami repo for postgres
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

