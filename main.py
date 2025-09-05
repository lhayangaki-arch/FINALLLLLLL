import os
import sys
from pathlib import Path

# Add the parent directory of src to the Python path
# This is crucial for imports like `from src.models import db` to work
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Import your Flask app instance from src/main.py
from main import app as flask_app

# Import the Netlify WSGI handler
# You will need to install `flask-lambda` or `serverless-wsgi`
# For this example, we'll use `flask_lambda` as it's simpler.
# pip install flask-lambda
from flask_lambda import FlaskLambda

# Wrap your Flask app with FlaskLambda
app = FlaskLambda(flask_app)

# The `app` object (which is now a FlaskLambda instance) will be the entry point
# for the Netlify Function. Netlify will automatically detect and use it.


