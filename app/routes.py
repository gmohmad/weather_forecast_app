from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from flask_login import logout_user

from app import app, db, forms
from app.models import User


@app.route('/')
def main():
    context = {}
    return render_template('main.html', context=context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))

    form = forms.LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main'))

    form = forms.SignupForm()

    if form.validate_on_submit():

        user = User(
            username=form.username.data,
            email=form.email.data,
            comfortable_temperature=form.comfortable_temperature.data
        )

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
