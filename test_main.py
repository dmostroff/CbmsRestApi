from fastapi.testclient import TestClient
import json

import app

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == { 'msg': 'Welcome to CBMS'}

def test_login():
    login_data = { 'username': 'jocko', 'pwd': 'ayecarumba'}
    response = client.post('/login', data=json.dumps(login_data))
    assert response.status_code == 200
    retval = response.json()
    assert retval['username'] == 'jocko'

# def test_read_clients():
#     response = client.get( '/clients')
#     assert response.status_code == 200
#     print( response)
    # assert len(response) == 45
