from fastapi import Body, FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
            "message":"Hello World!",
            "status":"OK"
            }

