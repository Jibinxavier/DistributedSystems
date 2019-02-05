import pytest
from flask import g, session 
from server import UserDb

from test_utils import TestUserDb 

def test_signup(client, app):
    # test that signup API is active 
    
    assert client.get('/user/signup').status_code == 200

    # test that successful registration redirects to the login page
    response = client.post(
        '/user/signup', data={'username': 'a', 'password': 'a'}
    )
    

    # test that the user was inserted into the database
    

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/user/signup',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get('/user/login').status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


 

@pytest.fixture
def client():
    
    import server

    client = server.app.test_client()
    db = TestUserDb()
    
    yield (client,db)
    db._clear_collection()