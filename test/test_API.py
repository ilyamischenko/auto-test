import requests

def test_api():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100