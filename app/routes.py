from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, forms


@app.route('/')
def main():
    context = {}
    return render_template('main.html', context=context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main'))

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    email = request.form.get('email')
    comfortable_temperature = request.form.get('comfortable_temperature')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('signup'))

    new_user = User(
        email=email,
        username=username,
        comfortable_temperature=comfortable_temperature,
        password=generate_password_hash(password, method='sha256')
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    return 'Logout'


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
