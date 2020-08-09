import json

import requests


class TestDeleteUser:
    def test_delete_user(self):
        user_id = create_user()
        response = requests.delete(
            "http://127.0.0.1:5000/api/users/" + user_id,
            headers={"Content-Type": "application/json"},
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

    return user_id
