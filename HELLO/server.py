from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
async def root(): 
    return {"menssagem": "Olá FastAPI - TDS 2025/1"}

@app.get('/profile')
def profile():
    return {'nome': 'Victória Amaral'}