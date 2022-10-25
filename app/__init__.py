from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes.routes import bp_cats, bp_dogs
    app.register_blueprint(bp_cats)
    app.register_blueprint(bp_dogs)

    return app