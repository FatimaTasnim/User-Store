import json

import requests

user_id = None


class TestCreateUser:
    def test_create_parent(self):
        payload = json.dumps(
            {
                "first_name": "miknew",
                "last_name": "lockwood",
                "role": "PARENT",
                "state": "US",
                "city": "NY",
                "zip": "2112",
            }
        )

        response = requests.post(
            "http://127.0.0.1:5000/api/users",
            headers={"Content-Type": "application/json"},
            data=payload,
        )
        user_id = response.json()["user_id"]
        print(response)
        assert response.status_code == 201

    def test_create_child(self):
        user_id = test_create()
        payload = json.dumps(
            {
                "first_name": "Finn",
                "last_name": "lockwood",
                "role": "CHILD",
                "parent": user_id,
            }
        )

        response = requests.post(
            "http://127.0.0.1:5000/api/users",
            headers={"Content-Type": "application/json"},
            data=payload,
        )
        assert response.status_code == 201

    def test_create_child_failed(self):
        payload = json.dumps(
            {
                "first_name": "Finn",
                "last_name": "lockwood",
                "role": "CHILD",
                "parent": "jasjdafja",
            }
        )

        response = requests.post(
            "http://127.0.0.1:5000/api/users",
            headers={"Content-Type": "application/json"},
            data=payload,
        )
        assert response.status_code == 400


def test_create():
    payload = json.dumps(
        {
            "first_name": "miknew",
            "last_name": "lockwood",
            "role": "PARENT",
            "state": "US",
            "city": "NY",
            "zip": "2112",
        }
    )

    response = requests.post(
        "http://127.0.0.1:5000/api/users",
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    user_id = response.json()["user_id"]
    return response.json()["user_id"]
