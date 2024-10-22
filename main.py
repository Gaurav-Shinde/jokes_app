from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

'''
Simple API to request a random joke per page refresh or button click.
'''

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Fetch a joke from the /joke endpoint
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/joke")
        joke = response.json()
    
    return templates.TemplateResponse("index.html", {"request": request, "joke": joke["joke"]})

@app.get("/joke")
async def get_joke():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://v2.jokeapi.dev/joke/Any?format=json")
        joke = response.json()
        if joke['type'] == 'single':
            return {"joke": joke['joke']}
        else:
            return {"joke": f"{joke['setup']} - {joke['delivery']}"}