# Importa a classe FastAPI do módulo fastapi
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Rota GET que recebe um nome como parâmetro da URL
@app.get("/saudacao/{nome}") 
async def root(nome: str):
    # Cria uma saudação personalizada com o nome recebido
    texto = f'Olá {nome}, tudo em paz?' 
    # Retorna a mensagem como resposta JSON
    return {"mensagem": texto}

# Rota GET que recebe um número pela URL e retorna seu quadrado
@app.get("/quadrado/{numero}")
def quadrado(numero: int):
    # Calcula o quadrado do número
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}.'
    return {"mensagem": texto}

# Rota GET que espera um número via query parameter (ex: /dobro?numero=5)
@app.get("/dobro")
def dobro(numero: int):
    # Calcula o dobro do número
    resultado = numero * 2
    texto = f'O dobro de {numero} é {resultado}.'
    return {"mensagem": texto}

# Rota GET que calcula a área de um retângulo usando parâmetros de query
# Exemplo: /area-retangulo?largura=5&altura=3
@app.get("/area-retangulo")
def area_retangulo(largura: int, altura: int = 1):
    # Calcula a área com base na largura e altura
    area = largura * altura
    texto = f'A área é {area}.'  # Pode ser melhorada a mensagem!
    return {"mensagem": texto}
