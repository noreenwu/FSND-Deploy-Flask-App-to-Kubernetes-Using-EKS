'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'commonstr'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk0NTY4NzMsIm5iZiI6MTU3ODI0NzI3MywiZW1haWwiOiJub3JlZW53dUBnbWFpbC5jb20ifQ.JIW4_8F4dNLPWfR-KoogCTeHXvrsaBGIGgJ9-ZD_1RI'
EMAIL = 'noreenwu@gmail.com'
PASSWORD = 'poppy'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    assert 0 3iel dkf

def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
