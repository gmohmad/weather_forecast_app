## To start the project follow these steps

### Set environment variable

#### Windows
```
set FLASK_APP=run.py
```

#### Linux/macOS
```
export FLASK_APP=run.py
```

### Create migrations (skip this step)
```
flask db init
```

### Execute migrations
```
flask db migrate -m "Initial migration"
```

### Apply migrations
```
flask db upgrade
```

### Run the app
```
flask run
```

### If telegram bot is not starting run this command
```
python chatbot/chatbot.py
```
