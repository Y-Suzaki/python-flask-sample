import json
from flask import Flask, render_template, session, redirect, url_for, flash, abort
from form import SignupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'xNVg}f_m:UmiOB{9bC`SvB9j5N<-3I./'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-sample.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    return 'Index'


@app.route('/api/hello')
def api_hello():
    session['username'] = 'Y-Suzaki'
    return "Hello,World."


@app.route('/api/users', methods=['GET'])
def api_users():
    return json.dumps({'names': ['Y-Suzaki', 'A-Tanaka', 'B-Hayashi']})


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('同名のユーザーが登録済みです。')
            return redirect(url_for('.signup'))
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('ユーザー登録が完了しました。ログインして下さい')
        return redirect(url_for('.signup'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('.dashboard'))
        flash('ユーザーまたはパスワードが一致しません。')
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    message = 'Python Flask Sampleのダッシュボードです。'
    history = '更新履歴です。'
    return render_template('dashboard.html', message=message, history=history)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
