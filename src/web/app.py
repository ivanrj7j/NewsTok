from flask import Flask
from src.web.front import frontend
from src.web.back import backend

app = Flask(__name__)
app.register_blueprint(frontend)
app.register_blueprint(backend)