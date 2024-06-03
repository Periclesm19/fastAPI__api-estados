from .main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_obter_estados():
    response = client.get(f'/api/v1/estados')
    assert response.status_code == 200
    assert response.json() is not None
    
    
def test_obter_estados_ordenados_por_id_decrescente():
    response = client.get(f'/api/v1/estados/descrescente')
    estados = response.json()
    assert response.status_code == 200
    assert response.json() is not None
    assert estados[0]['id'] > estados[1]['id']
    
    
def test_obter_estado_por_id():
    id = 11
    response = client.get(f'/api/v1/estado/{id}')
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()['id'] == id
    
def test_obter_estados_filtrados_por_regiao():
    regiao = 'Nordeste'
    response = client.get(f'/api/v1/estados/{regiao}')
    assert response.status_code == 200
    
    estados = response.json()
    assert estados is not None
    assert estados[0]['regiao']['nome'] == regiao
    
