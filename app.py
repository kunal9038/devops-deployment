from flask import Flask, render_template_string

app = Flask(__name__)

login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Login</title>
</head>
<body>
    <h2>DevOps Demo Login</h2>
    <form>
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

@app.route("/")
def login():
    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
