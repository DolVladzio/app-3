from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask-3 inside Docker!"

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/ready')
def ready():
    # Check database connection, etc.
    return {'status': 'ready'}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
