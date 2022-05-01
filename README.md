## Для запуска проекта выполните следующие команды

### Установите переменную среды

#### В Windows
```
set FLASK_APP=run.py
```

#### В Linux и macOS
```
export FLASK_APP=run.py
```

### Создайте миграции (пропустите этот шаг)
```
flask db init
```

### Выполните миграции
```
flask db migrate -m "Initial migration"
```

### Примените миграции
```
flask db upgrade
```

### Запустите приложение выполнив команду ниже
```
flask run
```
