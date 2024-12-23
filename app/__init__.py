from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy extension
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app
