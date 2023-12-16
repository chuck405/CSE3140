from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Q3.JS")

if __name__ == "__main__":
    app.run(debug=True)