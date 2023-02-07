## Prerequisites
- python3
- docker
- minikube
- kubectl


## Run application
The image repo is public, you should be able to pull from it. If you would like to pull from your docker hub then build, tag and push the image stated below. 
####(Optional) Build and tag and push the docker image (login to your docker hub to push)

docker build -t flask-kubernetes . 

docker tag flask-kubernetes yourDockerHub/flask-kubernetes:latest

docker push 

###Deploy the app
kubectl apply -f deployment.yaml 

Ensure the pods are running - kubectl get pods

##Accessing the app
kubectl port-forward deployments/flask-test-app 5020:5000

Then go to your browser and enter this endpoint: localhost:5020


