from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
async def root(): 
    return {"menssagem": "Olá FastAPI - TDS 2025/1"}