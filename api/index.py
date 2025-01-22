# app.py (Flask example)
from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return "Internal Server Error", 500

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Server Error: {error}, Route: {request.url}")
    return "500 error: Internal Server Error", 500

@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(f"Page Not Found: {error}, Route: {request.url}")
    return "404 error: Page Not Found", 404

if __name__ == "__main__":
    app.run(debug=True)