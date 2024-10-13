from flask import Flask
from flask_cors import CORS  # Import CORS
from flask_migrate import Migrate
from .database import db  # Import db from the new database module

def create_app():
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)  # Enable CORS

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import models
    from .models import Product  # Ensure models are imported here

    # Register blueprints
    from .routes import init_routes
    init_routes(app)

    # Shell context for Flask CLI
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'Product': Product}

    return app
