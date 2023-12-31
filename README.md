# jenkins-app

# First of all need to pull a container from docker hub:

docker pull silverpunkn/myjenkins-blueocean


# Create a network 'jenkins':

docker network create jenkins


# To run a docker containe on MacOS/Linuxr need to use this command:

docker run --name jenkins-blueocean --restart=on-failure --detach \\\
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \\\
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \\\
  --publish 8080:8080 --publish 50000:50000 \\\
  --volume jenkins-data:/var/jenkins_home \\\
  --volume jenkins-docker-certs:/certs/client:ro \\\
  silverpunkn/myjenkins-blueocean


# For Windows:

docker run --name jenkins-blueocean --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 silverpunkn/myjenkins-blueocean


# Get the Password:

docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword


# Connect to the Jenkins:

https://localhost:8080/
