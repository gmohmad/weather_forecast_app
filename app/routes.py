from datetime import date, datetime

import requests
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from flask_login import logout_user

from app import app, db
from app.models import User
from app.forms import SignupForm, LoginForm
from app.utils import get_weather_data, is_comfortable_temperature


@app.route('/')
def main():

    weather_data = get_weather_data('Грозный')

    current_date = datetime.strftime(date.today(), '%d %B %Y')
    temp = weather_data.get('main', {}).get('temp', '?')
    weather = weather_data.get('weather', [])
    country = weather_data.get('sys', {}).get('country', '?')
    comfortable_temperature = is_comfortable_temperature(current_user, temp)

    if weather_data.get('weather', []):
        weather = weather[0].get('main', '?')
    else:
        weather = '?'

    context = {
        'date': current_date,
        'city': 'Grozny',
        'temp': temp,
        'weather': weather,
        'country': country,
        'is_comfortable_temperature': comfortable_temperature,
    }

    return render_template('main.html', context=context)


@app.route('/valute', methods=['GET'])
def valute():
    API_ENDPOINT = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(API_ENDPOINT).json()

    USD = response.get('Valute', {}).get('USD', {}).get('Value')
    EUR = response.get('Valute', {}).get('EUR', {}).get('Value')

    context = {
        'USD': USD,
        'EUR': EUR
    }

    return render_template('valute.html', context=context)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main'))

    form = LoginForm()

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

    form = SignupForm()

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
