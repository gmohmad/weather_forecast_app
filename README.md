export FLASK_APP=run.py
flask run

flask db init
flask db migrate -m "Initial migration."
flask db upgrade