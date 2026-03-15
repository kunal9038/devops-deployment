from flask import Flask, render_template_string

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Login</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body{
            margin:0;
            padding:0;
            height:100vh;
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
            display:flex;
            justify-content:center;
            align-items:center;
            overflow:hidden;
        }

        /* Animated Background Circles */
        .circle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255,255,255,0.05);
            animation: float 15s infinite;
        }
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-200px) rotate(180deg); }
            100% { transform: translateY(0) rotate(360deg); }
        }

        .login-box{
            background:white;
            padding:40px;
            border-radius:10px;
            width:350px;
            box-shadow:0px 0px 30px rgba(0,0,0,0.5);
            position: relative;
            z-index: 1;
        }

        h2{
            text-align:center;
            color:#333;
        }

        input{
            width:100%;
            padding:12px;
            margin-top:10px;
            border-radius:5px;
            border:1px solid #ccc;
            font-size: 14px;
        }

        button{
            width:100%;
            padding:12px;
            margin-top:20px;
            background:#007BFF;
            color:white;
            border:none;
            border-radius:5px;
            font-weight:bold;
            cursor:pointer;
            transition: all 0.3s ease;
        }
        button:hover{
            background:#0056b3;
            transform: scale(1.05);
            box-shadow: 0 0 10px #007BFF;
        }

        .tech-text{
            text-align:center;
            margin-bottom:15px;
            color:#555;
        }

        .extra-links{
            display:flex;
            justify-content: space-between;
            font-size: 12px;
            margin-top: 10px;
        }
        .extra-links a{
            color:#007BFF;
            text-decoration: none;
        }
        .extra-links a:hover{
            text-decoration: underline;
        }

        /* Flash messages */
        .flash {
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            text-align: center;
        }
    </style>
</head>

<body>
    <!-- Background circles -->
    <div class="circle" style="width:200px;height:200px;top:50px;left:30px;"></div>
    <div class="circle" style="width:150px;height:150px;top:200px;right:50px;"></div>
    <div class="circle" style="width:300px;height:300px;bottom:50px;left:100px;"></div>

    <div class="login-box">
        <h2>DevOps Login</h2>
        <p class="tech-text">CI/CD Pipeline Test</p>

        {% with messages = get_flashed_messages() %}
          {% if messages %}
            {% for message in messages %}
              <div class="flash">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            
            <div class="extra-links">
                <label><input type="checkbox" name="remember"> Remember Me</label>
                <a href="#">Forgot Password?</a>
            </div>

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
