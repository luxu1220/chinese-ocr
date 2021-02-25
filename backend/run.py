from flask import Flask
from constants import APP_SECRET_KEY
from route.init_api import api

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY

api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
