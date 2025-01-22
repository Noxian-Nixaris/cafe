# cafe

Стек использованных технологий.
Python 3.12.7, Django 5.1.5, HTML, bootstrap5


## Установка:
```
git clone  https://github.com/Noxian-Nixaris/cafe.git
cd cafe
```


### Cоздать и активировать виртуальное окружение:

#### Windows
```
python -m venv venv
source venv/Scripts/activate
```
#### Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```
### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### Выполнить миграции:

#### Windows
```
python manage.py makemigrations
python manage.py migrate
```
#### Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Запустить проект:

#### Windows
```
python manage.py runserver
```
#### Linux/macOS
```
python3 manage.py runserver
```
