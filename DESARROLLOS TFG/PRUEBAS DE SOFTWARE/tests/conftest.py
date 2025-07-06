import sys
from pathlib import Path

# Añadir el directorio raíz al path de Python
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from fastapi.testclient import TestClient
from api import app

@pytest.fixture
def client():
    """
    Fixture que proporciona un cliente de prueba para la API.
    Este cliente se puede usar en todas las pruebas.
    """
    return TestClient(app) 