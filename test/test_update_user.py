import json

import requests


class TestUpdateUser:
    def test_update_user(self):
        user_id = create_user()

        payload = json.dumps({"first_name": "Finn",})

        response = requests.patch(
            "http://127.0.0.1:5000/api/users/" + user_id,
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        assert response.status_code == 200

    def test_update_user_failed(self):
        user_id = create_user()

        payload = json.dumps({"role": "CHILD",})

        response = requests.patch(
            "http://127.0.0.1:5000/api/users/" + user_id,
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        assert response.status_code == 200


def create_user():
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
