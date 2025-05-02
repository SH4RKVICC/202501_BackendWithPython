from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
async def root(): 
    return {"menssagem": "Olá FastAPI - TDS 2025/1"}

@app.get('/profile')
def profile():
    return {'nome': 'Victória Amaral'}

@app.post('/profile')
def signup():
    return {'Mensagem': 'Perfil Criado Com Sucesso!'}

@app.put('/profile')
def atualizar():
    return {'Mensagem': 'Perfil Atualizado Com Sucesso!'}

@app.delete('/profile')
def delete():
    return {'Mensagem': 'Perfil Deletado Com Sucesso!'}