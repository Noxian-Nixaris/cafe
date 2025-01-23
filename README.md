# cafe

## Описание
Проект веб-приложение на Django для управления заказами в кафе. Приложение позволяет добавлять, удалять, искать, изменять и отображать заказы.

## Стек использованных технологий.
Python 3.12.7, Django 5.1.5, HTML, CSS


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
### загрузить фикстуры
```
python manage.py loaddata dish.json
```
Основные модели
### Запустить проект:

#### Windows
```
python manage.py runserver
```
#### Linux/macOS
```
python3 manage.py runserver
```
## Работа с проектом

Стартовая страница доступна по адресу 
```
/orders/
```
Здесь вы можете
* открыть новую смену
* закрыть текущую смену 
* рассчитать выручку для указанной смены

Страница создания заказа
```
/orders/create/
```
Здесь вы:
* вводите номер стола
* отмечаете блюда для заказа
* отправляете запрос "посчитать".

Страница заказа
```
/orders/{order_id}/
```
Здесь вы можете:
* изменить статус заказа на следующий если его статус еще не "оплачено"
    - ```/orders/{order_id}/status/```.
* перейти на форму редактирования заказа
    - ```/orders/{order_id}/edit/```
* удалить заказ
    - ```/orders/{order_id}/delete```

Страница редактирования заказа
```
/orders/{order_id}/edit/
```
Здесь вы можете:
* сменить номер стола
* убрать или добавить блюда
* пересчитать заказ

Страница со списком всех заказов
```
/orders/list/
```
Здесь вы можете:
отсортировать список заказов по номеру стола и по статусу заказа

Страница поиска заказов
```
/orders/search/
```
Здесь вы можете найти заказ по его ID

## Авторы
Владимир Рубец

