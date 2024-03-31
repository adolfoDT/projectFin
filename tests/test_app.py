import pytest
import fakeredis
from app import create_app


@pytest.fixture(scope="module")
def test_data():
    return {}

@pytest.fixture
def client(test_data):
    app = create_app()
    app.config['TESTING'] = True

    app.redis = fakeredis.FakeStrictRedis()

    with app.test_client() as client:
        yield client

def test_shorten_url(client, test_data):
    response = client.post('/shorten', data={'url': 'https://example.com'})
    assert 'Short URL' in response.data.decode()
    url = response.data.decode().split()[-1]
    test_data['short_url'] = '/' + url.rsplit('/', 1)[-1]

def test_redirect_to_original(client, test_data):
    client.post('/shorten', data={'url': 'https://example.com'})
    short_url = test_data.get("short_url")
    assert short_url is not None
    response = client.get(short_url) 
    assert response.status_code == 302
    assert response.location == 'https://example.com'
def test_link_stats_without_access(client):
    short_url = "def456"
    response = client.get(f'/stats/{short_url}')
    assert response.status_code == 404
    assert response.data.decode() == 'No access data found for this short link.'

