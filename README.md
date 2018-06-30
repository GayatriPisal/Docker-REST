# Docker-REST
Implement RESTful web service with Flask and Python

Docker makes it possible to get far more apps running on the same old servers and it also makes it very easy to package and ship programs. Docker uses containers and images to address every application across the hybrid cloud.

This program uses a docker to implement RESTful API with the help of Flask and Python.

Step to follow:

1. Install Docker.[https://www.docker.com]

2. Create Docker Image by running : "docker build -t flaskapp ."

3. Check the created image using "docker images"

4. Run the docker image inside the docker container using the command: "docker run -d -p 5000:5000 flaskapp"

5. Check the running docker container : "docker ps"

6. App will be running on this address : http://0.0.0.0:5000. [5000 is the default port for Python]

