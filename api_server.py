from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'cofeek-322'
api = Api(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
