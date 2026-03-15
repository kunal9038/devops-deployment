from flask import Flask, render_template_string

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html>
<head>
<title>DevOps Login</title>
<style>
body {
    font-family: Arial;
    background-color: #f2f2f2;
    text-align: center;
}

.container {
    margin-top: 100px;
    background: white;
    padding: 30px;
    width: 300px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 10px;
    box-shadow: 0px 0px 10px gray;
}

input {
    width: 90%;
    padding: 8px;
    margin: 8px;
}

button {
    padding: 10px 20px;
    background: green;
    color: white;
    border: none;
}
</style>
</head>

<body>

<div class="container">
<h2>DevOps Login Page 🚀</h2>
<p>CI/CD Test Version</p>

<form>
<input type="text" placeholder="Username"><br>
<input type="password" placeholder="Password"><br>
<button type="submit">Login</button>
</form>

</div>

</body>
</html>
"""

@app.route("/")
def login():
    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
