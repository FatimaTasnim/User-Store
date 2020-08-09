from flask import Flask, request, Response
from database.db import initialize_db
from database.models import User


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/userStore'
}


initialize_db(app)


@app.route('/api/users', methods=['POST'])
def add_user():
    body = request.get_json()
    user = User()
    user['first_name'] = body['first_name']
    user['last_name'] = body['last_name']
    user['role'] = body['role']

    if body['role'] == 'PARENT':
        if 'street' in body:
            user['street'] = body['street']
        if 'state' in body:
            user['state'] = body['state']
        if 'city' in body:
            user['city'] = body['city']
        if 'zip' in body:
            user['zip'] = body['zip']
        user.save()
        return "Your data is stored properly", 200
    elif body['role'] == 'CHILD':
        try:
            body['parent']
            if body['parent'] == "":
                return {'error': "please enter parent id"}, 400
            try:
                User.objects.get(user_id=body['parent'])
                user['parent'] = body['parent']
                user.save()
                return "Your data stored properly", 201
            except:
                return {'error': "please enter a registered parent id"}, 400
        except:
            return {'error': "please enter parent id"}, 400

app.run()