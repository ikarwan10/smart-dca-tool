# WSGI entry point for PythonAnywhere
# This file is used by PythonAnywhere to run the Flask app

import sys
import os

# Add the project directory to the path
project_home = '/home/YOUR_USERNAME/DCA'  # Change YOUR_USERNAME to your PythonAnywhere username
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application
