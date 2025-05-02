# Importa a classe FastAPI do módulo fastapi
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define uma rota GET para a raiz do site ("/")
@app.get("/") 
async def root(): 
    # Retorna uma mensagem como resposta em formato JSON
    return {"menssagem": "Olá FastAPI - TDS 2025/1"}

# Define uma rota GET para "/profile"
@app.get('/profile')
def profile():
    # Retorna um dicionário com o nome, como uma simulação de perfil
    return {'nome': 'Victória Amaral'}

# Define uma rota POST para "/profile"
@app.post('/profile')
def signup():
    # Simula a criação de um perfil e retorna uma mensagem de sucesso
    return {'Mensagem': 'Perfil Criado Com Sucesso!'}

# Define uma rota PUT para "/profile"
@app.put('/profile')
def atualizar():
    # Simula a atualização de um perfil e retorna uma mensagem de sucesso
    return {'Mensagem': 'Perfil Atualizado Com Sucesso!'}

# Define uma rota DELETE para "/profile"
@app.delete('/profile')
def delete():
    # Simula a exclusão de um perfil e retorna uma mensagem de sucesso
    return {'Mensagem': 'Perfil Deletado Com Sucesso!'}
