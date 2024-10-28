# Microservices Application

This project demonstrates a microservice-based application deployed using Kubernetes. The application consists of two microservices and a PostgreSQL database. The microservices are designed to handle user data and generate random numbers. The user needs to be created using the user service and then the user can be used to generate random numbers.


## Microservices

1. **User Service**: Manages user data.
2. **Random Number Service**: Generates random numbers.

## Software Architecture Design

### Components and Responsibilities

1. **User Service**:
    - **Role**: Manages user data.
    - **Responsibilities**:
        - Create new users.
        - Retrieve user information.
    - **Microservice**: `user_service.py`
    - **Endpoints**:
        - `POST /users`: Create a new user.
        - `GET /users`: Retrieve all users.

2. **Random Number Service**:
    - **Role**: Generates random numbers for users.
    - **Responsibilities**:
        - Generate random numbers based on user input.
        - Retrieve saved random numbers.
    - **Microservice**: `generate-random-number.py`
    - **Endpoints**:
        - `POST /generate-random-number`: Generate a random number for a user.
        - `GET /get-saved-numbers`: Retrieve all saved random numbers.

3. **PostgreSQL Database**:
    - **Role**: Stores user data and generated random numbers.
    - **Responsibilities**:
        - Persist user information.
        - Persist generated random numbers.
    - **Deployment**: Managed using Helm charts.

### Architecture Principles

- **Microservices Architecture**: Each service is independently deployable and scalable.
- **Containerization**: Services are containerized using Docker.
- **Orchestration**: Kubernetes is used for orchestration and management of containers.
- **Deployment**: Helm charts are used for deploying services and managing dependencies.
- **Database**: PostgreSQL is used as the database for persistent storage.

### Benefits and Challenges

#### Benefits

- **Scalability**: Each microservice can be scaled independently based on load.
- **Maintainability**: Services are loosely coupled, making it easier to maintain and update.
- **Resilience**: Failure in one service does not affect the others.

#### Challenges

- **Complexity**: Managing multiple services can be complex activity. Hence, helm charts are used to manage the deployment.
- **Security**: The services need to be prevented from unauthorised access using cloud native api gateway. This would depend on which cloud they are deployed on for example api gateway on AWS. 

### Security Considerations

- **Authentication and Authorization**: Security and other related controls would be applied on the cloud level using the cloud native api gateways.
- **Data Encryption**: Encrypting sensitive data both in transit and at rest can be done. 

### Mitigation Strategies

- **Monitoring and Logging**: Implementing centralized logging and monitoring to detect and respond to issues quickly can be done using cloud native technologies.
- **Regular Security scans**: Conducting regular security audits and vulnerability assessments.

## Prerequisites

- Docker
- Kubernetes
- kubectl
- Helm

## Setup

### 1. Build and Push Docker Images

Navigate to the `backend` directory and build the Docker images for each service:

```sh
# Build and push User Service
cd backend
docker build -t user_service -f docker/user_service/Dockerfile .
docker push user_service

# Build and push Random Number Service
docker build -t random_service -f docker/random_service/Dockerfile .
docker push random_number_service

# get bitnami repo for postgres
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# update the dependencies after navigating to the chart directory
helm dependency update 

```
### 2. Deploy the helm chart
```sh
cd helm/random
helm upgrade --install --namespace test app .


```
You can use the commands displayed after the above command to port forward the services to access them locally. 

```sh

### 3. Access the Services
```sh
curl --request GET \
--url http://localhost:8081/users 


curl --request POST \
  --url http://localhost:8081/users \
  --header 'Content-Type: application/json' \
  --data '{
	"name":"ankur"
}'

curl --request GET \
  --url http://localhost:8080/get-saved-numbers 
  
curl --request POST \
  --url http://localhost:8080/generate-random-number \
  --header 'Content-Type: application/json' \
  --data '{
	"user":"ankur"
}'
```

### 4. Clean Up
```sh
helm uninstall app --namespace test
```