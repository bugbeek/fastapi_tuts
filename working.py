from fastapi import Body, FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Data": "This is your home section"}

@app.get('/about')
def about():
    return {"Data":"This is your about section"}

@app.post('/createpost')
def create_post(payload : dict = Body(...)):
    print(payload)
    return {"Data": "This is your create post section"}