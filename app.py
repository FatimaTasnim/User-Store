from flask import Flask
from database.db import initialize_db


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/userStore'
}


initialize_db(app)


app.run()