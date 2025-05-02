from fastapi import FastAPI

app = FastAPI()


@app.get("/saudacao/{nome}") 
async def root(nome: str):
    texto = f'Olá {nome}, tudo em paz?' 
    return {"mensagem": texto}

@app.get("/quadrado/{numero}")
def quadrado(numero:int):
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}.'
    return {"mensagem": texto}