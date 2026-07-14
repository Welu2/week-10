"""
Flask Application

Task 3
Brent Oil Price Dashboard

Author: Your Name
"""

from flask import Flask
from flask_cors import CORS

from routes import api


def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)

    # Allow React frontend to access API
    CORS(app)

    # Register API routes
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/")
    def home():
        return {
            "project": "Brent Oil Price Dashboard",
            "version": "1.0.0",
            "status": "running"
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )