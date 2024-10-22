# Jokes App
## App Development
#### Environment Setup
Platform: Windows 10 Home Edition
Binaries
- Python 3.9.7

### Start Application
1. cd jokes_app
2. python -m venv venv
3. .\venv\Scripts\activate
4. pip install -r requirements.txt
5. uvicorn main:app --reload
6. http://127.0.0.1:8000/

### Stop Application
1. cntrl + c in terminal process running api server
2. deactivate


## Docker Development
#### Environment Setup
-   NAME="Linux Mint"
    VERSION="21.2 (Victoria)"
    ID_LIKE="ubuntu debian"
    VERSION_ID="21.2"
-   Docker version 24.0.7

### Start Application
1. cd jokes_app
2. sudo -i
2. docker build -t jokes-app:latest .
3. docker run -d -p \<your host port\>:8000 --name jokes-app-container  jokes-app
4. http://127.0.0.1:8000/

### Stop Application Container(s)
1. docker ps -a | awk 'NR == 1 || /jokes-app/'
2. docker rm \$(docker stop \$(docker ps -a -q --filter ancestor="jokes-app" --format="{{.ID}}"))


## Kubernetes Cluster
### Environment Setup
-   minikube version: v1.31.2
-   Client Version: version.Info{Major:"1", Minor:"26", GitVersion:"v1.26.15", GitCommit:"1649f592f1909b97aa3c2a0a8f968a3fd05a7b8b", GitTreeState:"clean", BuildDate:"2024-03-14T01:05:39Z", GoVersion:"go1.21.8", Compiler:"gc", Platform:"linux/amd64"}
Kustomize Version: v4.5.7

### Start Kubernetes Cluster


#### Created by Gaurav Shinde

