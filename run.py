import json
from flask import Flask, render_template, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'xNVg}f_m:UmiOB{9bC`SvB9j5N<-3I./'


@app.route("/api/hello")
def api_hello():
    session['username'] = 'Y-Suzaki'
    return "Hello,World."


@app.route("/api/users", methods=['GET'])
def api_users():
    return json.dumps({'names': ['Y-Suzaki', 'A-Tanaka', 'B-Hayashi']})


@app.route("/dashboard", methods=['GET'])
def dashboard():
    message = 'Python Flask Sampleのダッシュボードです。'
    history = '更新履歴です。'
    return render_template('dashboard.html', message=message, history=history)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
