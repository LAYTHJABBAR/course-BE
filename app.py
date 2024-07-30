from flask import Flask
from config import Config
from pymongo import MongoClient
from routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    client = MongoClient(app.config['MONGO_URI'])
    db = client[app.config['MONGO_DBNAME']]

    app.register_blueprint(main, url_prefix='/api')

    return app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
