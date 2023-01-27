from flask import Flask
from src.routes.endpoints import register_blueprint


def create_app(**flask_configs):
    app = Flask(__name__, template_folder="src/templates")
    register_blueprint(app)

    return app



if __name__ == "__main__":
    app = create_app()
