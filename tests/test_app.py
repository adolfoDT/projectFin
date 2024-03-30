import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_shorten_url(client):
    response = client.post('/shorten', data={'url': 'https://example.com'})
    assert 'Short URL' in response.data.decode()

def test_redirect_to_original(client):
    client.post('/shorten', data={'url': 'https://example.com'})
    response = client.get('/abcdef')  # Use the correct short URL
    assert response.status_code == 302
    assert response.location == 'https://example.com'

