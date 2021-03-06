import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    secret = app.config.get('SECRET_KEY')
    return f"This is my secret password: {secret}, but shhhh ..."
