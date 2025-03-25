# Dockerized Flask Notebook App

A containerized Flask application with persistent SQLite database storage.

## Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Terminal/shell access

## Quick Start

### 1. CLone
Clone this repository to your computer using ([this link](https://github.com/1192119703jzx/cs217-assignments.git)) and open folder Assignment3. 

### 2. Build the Docker Image
```bash
docker build -t notebook-app .
```
This will :
* Creates an image named notebook-app using the Dockerfile in current directory
* Installs Python dependencies via requirements.txt
* your can modify notebook-app to any name you want for the image

### 3. Run the Container with Persistent Database
```bash
docker run -v $(pwd)/container_db:/app/instance -p 5000:5000 notebook-app
```
This will:
* Creates a container_db folder on your host machine in current directory
* Maps it to /app/instance in the container (where Flask stores SQLite DB)
* Ensures database survives container restarts/deletion


### 4. Access
Access the application with your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)