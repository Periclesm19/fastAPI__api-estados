from typing import List
from fastapi import FastAPI, Query
import requests

from models import Estado

app = FastAPI(title= 'Estados do Brasil API', docs_url='/api/v1')
URL = 'https://brasilapi.com.br/api/ibge/uf/v1'

@app.get('/api/v1/estados', response_model=List[Estado] , tags=['Estados'], summary='Obter todos o estados.', name='Estados do Brasil')
def obter_estados():
    response = requests.get(URL)
    estados = []
    
    if response.status_code == 200:
        dados = response.json()
        
        for estado in dados:
            estados.append(estado)
            
    return estados


@app.get('/api/v1/estados/descrescente', response_model=List[Estado] , tags=['Estados'], summary='Obter todos os estados ordenados por id de forma decrescente.')
def obter_estados_ordenados_por_id_decrescente():
    response = requests.get(URL)
    estados = []
    
    if response.status_code == 200:
        dados = response.json()
        
        for estado in dados:
            estados.append(estado)
            
    estados.sort(key=lambda estado: estado['id'], reverse=True)
            
    return estados


@app.get('/api/v1/estado/{id}', response_model=Estado , tags=['Estados'], summary='Obter estado por id.')
def obter_estado_por_id(id: int = Query):
    response = requests.get(URL)
    estado_por_id = {}
    
    if response.status_code == 200:
        dados = response.json()
        
        for estado in dados:
            if estado['id'] == id:
                estado_por_id = estado                       
                
    return estado_por_id


@app.get('/api/v1/estados/{regiao}', response_model=List[Estado] ,tags=['Estados'], summary='Obter estados por região.')
def obter_estados_filtrados_por_regiao(regiao: str = Query):
    response = requests.get(URL)
    estados_por_regiao = []
    
    if response.status_code == 200:
        dados = response.json()
        
        for estado in dados:
            if estado['regiao']['nome'] == regiao.capitalize():
                estados_por_regiao.append(estado)                            
                
    return estados_por_regiao
    
        