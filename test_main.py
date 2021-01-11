from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == { 'msg': 'Welcome to CBMS'}

def test_read_client_persons():
    response = client.get( '/client/person')
    assert response.status_code == 200
    print( response)
    # assert len(response) == 45
