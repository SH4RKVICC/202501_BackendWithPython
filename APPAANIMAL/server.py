from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get('/animais')
def lista_animais():
    return banco

@app.get('/animais/{animal_id: str}')
def obter_animal(animal_id: str,):
    for animal in banco:
        if animal.id - animal_id:
            return animal
    return {'erro': 'Animal NÃO localizado.'} 

@app.post()
def criar_animai(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None