"""
Smart DCA Investment Tool - Main Application
=============================================
Flask application entry point.
"""

from flask import Flask, jsonify
from config import config
import os

# Initialize Flask app
app = Flask(__name__, 
            template_folder='app/templates',
            static_folder='app/static')

# Load configuration
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Initialize database
from app.models.models import db
db.init_app(app)

# Import routes after app is created to avoid circular imports
from app.routes import main_routes, api_routes, portfolio_routes, settings_routes

# Register blueprints
app.register_blueprint(main_routes.bp)
app.register_blueprint(api_routes.bp, url_prefix='/api')
app.register_blueprint(portfolio_routes.bp, url_prefix='/api')
app.register_blueprint(settings_routes.bp, url_prefix='/api')


@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'version': '1.0.0'})


# Create database tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
