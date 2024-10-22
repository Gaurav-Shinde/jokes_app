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
3. docker run -d --rm -m 6MB -p \<your host port\>:8000 --name jokes-app-container  jokes-app
4. http://127.0.0.1:8000/

### Stop Application Container(s)
1. docker ps
2. docker rm \$(docker stop \$(docker ps -a -q --filter ancestor=\<image-name\> --format="{{.ID}}"))

#### Created by Gaurav Shinde

