import pytest
import requests

url = 'http://127.0.0.1:5000'

class TestSearchUsers():
    def test_all_users(self):
        r = requests.get(url+'/api/users')
        assert r.status_code == 200
    