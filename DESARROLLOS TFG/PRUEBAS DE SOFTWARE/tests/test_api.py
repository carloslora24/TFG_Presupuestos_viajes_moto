import json
import pytest
from pathlib import Path

# Cargar los datos de prueba
def load_test_data(filename):
    with open(Path(__file__).parent / filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Prueba del formato de respuesta con datos válidos
def test_presupuesto_formato_completo(client):
    # Cargar datos válidos
    datos_validos = load_test_data('datos_validos.json')
    
    # Realizar la petición POST
    response = client.post("/presupuestovm", json=datos_validos)
    
    # Verificar el código de estado
    assert response.status_code == 200
    
    # Verificar la estructura de la respuesta
    data = response.json()
    assert "status" in data
    assert "data" in data
    assert data["status"] == "success"

# Prueba del manejo de errores con datos inválidos
def test_presupuesto_datos_invalidos(client):
    # Cargar datos inválidos
    datos_invalidos = load_test_data('datos_invalidos.json')
    
    # Realizar la petición POST
    response = client.post("/presupuestovm", json=datos_invalidos)
    
    # Verificar el código de estado
    assert response.status_code == 200
    
    # Verificar la estructura de la respuesta de error
    data = response.json()
    assert "status" in data
    assert "data" in data
    assert data["status"] == "error"
    assert isinstance(data["data"], str)  # El mensaje de error debe ser una cadena 