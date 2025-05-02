from fastapi import FastAPI

app = FastAPI()


@app.get("/saudacao/{nome}") 
async def root(nome): 
    return nome