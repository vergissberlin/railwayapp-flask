from flask import Flask

app = Flask(__name__)


@app.get("/")
@app.get("/health")
def health():
    return "ok\n", 200, {"Content-Type": "text/plain; charset=utf-8"}
