from flask import Flask

app = Flask(__name__)

APP_VERSION = "v2"


@app.route("/")
def home():
    return f"Hello from minikube-flask-app - version {APP_VERSION}\n"


@app.route("/health")
def health():
    return "ok\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
