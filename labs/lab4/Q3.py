from flask import Flask

app = Flask(__name__)
@app.route("/")
def team_info():
    return "<p>Team Number: 4, Team Names: Nguyen Truc Ho and Johnson Dorothea</p>"
