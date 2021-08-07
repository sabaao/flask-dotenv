import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
APP_ROOT = os.path.join(os.path.dirname(__file__),'..')
dotenv_path = os.path.join(APP_ROOT,'.env')
load_dotenv(dotenv_path)

app.config['TESTING'] = os.getenv('TESTING')

@app.route('/')
def hello_world():
    return os.getenv('FLASK_ENV')


app.run()