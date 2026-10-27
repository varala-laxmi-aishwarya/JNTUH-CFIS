from flask import Flask, render_template_string, request
import mysql.connector
import webbrowser

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Verification</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f4f4f9; }
        .box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); width: 300px; text-align: center; }
        input { width: 100%; padding: 8px; margin: 10px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; padding: 10px; background: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #45a049; }
        .message { margin-top: 15px; font-weight: bold; }
        .success { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Login Page</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="User ID" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        
        {% if message %}
            <div class="message {{ status }}">{{ message }}</div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    status = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost", user="root", password="root", database="login_creds_database"
        )
        cursor = db.cursor(dictionary=True)

        # --- THIS IS WHERE THE SQL QUERY RUNS ---
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] Executing Query: {query}")

        cursor.execute(query)
        user = cursor.fetchone()  # Fetches matching user if credentials are valid

        cursor.close()
        db.close()

        # Check result and set inline message on the same page
        if user:
            message = f"Access Granted! Welcome, {user['username']}."
            status = "success"
        else:
            message = "Access Denied! Invalid User ID or Password."
            status = "error"

    return render_template_string(HTML_PAGE, message=message, status=status)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
