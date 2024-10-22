Environment Setup
Platform: Windows 10 Home Edition
Binaries
- Python 3.9.7

Start Application
1. cd jokes_app
2. python -m venv venv
3. .\venv\Scripts\activate
4. pip install -r requirements.txt
5. uvicorn main:app --reload
6. https://localhost:8000/

Stop Application
1. cntrl + c in terminal process running api server
2. deactivate

Created by Gaurav Shinde

