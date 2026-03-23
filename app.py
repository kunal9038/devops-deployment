from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return """
    <h1 style='color:green;'>🚀 CI/CD Pipeline Working!</h1>
    <h2>DevOps Deployment Success ✅</h2>
    <p>Version 2 - Auto Deploy Test</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

