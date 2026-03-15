from flask import Flask, render_template_string

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html>
<head>
<title>DevOps Login</title>

<style>

body{
    margin:0;
    padding:0;
    height:100vh;
    font-family: Arial, Helvetica, sans-serif;

    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);

    display:flex;
    justify-content:center;
    align-items:center;
}

.login-box{
    background:white;
    padding:40px;
    border-radius:10px;
    width:300px;

    box-shadow:0px 0px 20px rgba(0,0,0,0.5);
}

h2{
    text-align:center;
    color:#333;
}

input{
    width:100%;
    padding:10px;
    margin-top:10px;
    border-radius:5px;
    border:1px solid #ccc;
}

button{
    width:100%;
    padding:10px;
    margin-top:20px;

    background:#007BFF;
    color:white;

    border:none;
    border-radius:5px;

    font-weight:bold;
    cursor:pointer;
}

button:hover{
    background:#0056b3;
}

.tech-text{
    text-align:center;
    margin-bottom:20px;
    color:#555;
}

</style>
</head>

<body>

<div class="login-box">

<h2>DevOps Login</h2>

<p class="tech-text">CI/CD Deployment Test</p>

<input type="text" placeholder="Username">

<input type="password" placeholder="Password">

<button>Login</button>

</div>

</body>
</html>

"""

@app.route("/")
def login():
    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
