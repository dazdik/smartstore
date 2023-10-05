# **Book for Coders**
### **Описание**
Интернет-магазин Book for Coders

**Особенности проекта:**

* Магазин с возможностью добавление товаров через админ-панель Джанго
* Платежная система **Stripe**
для "покупки" товара используйте карту `4242 4242 4242 4242`
* новый аккаунт после регистрации активируется путем отправки ссылки с токеном на эл.почту с использованием очереди задач (Celery) в качестве брокера сообщений выступает Redis.

Перейти в магазин по [ссылке](https://book-for-coders.ru/)

### **Технолгии**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)

<h3>Запуск проекта в dev-режиме</h3> 
<details><summary></summary>



#### *Клонируйте репозиторий:*

````
git clone https://github.com/dazdik/smartstore
`````

#### *Установите и активируйте виртуальное окружение:*
**Win**:
```
python -m venv venv
venv/Scripts/activate
```

**Mac**:
```
python3 -m venv venv
source venv/bin/activate
```
#### *Установите зависимости из файла requirements.txt и линтеры из requirements.lint.txt:*
```
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements.lint.txt
```
#### *Cоздайте файл .env и заполните его по следующему шаблону:*
```
DEBUG=True
SECRET_KEY=<сгенерировать секретный ключ для проекта>
DOMAIN_NAME=http://127.0.0.1:8000

REDIS_HOST=127.0.0.1
REDIS_PORT=6379

DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=<указать почту, с которой будут приходить письма новому пользователю для получения токена>
EMAIL_HOST_PASSWORD=<указать пароль от почты>
EMAIL_USE_SSL=True

STRIPE_PUBLIC_KEY=<https://stripe.com/docs/keys>
STRIPE_SECRET_KEY=<https://stripe.com/docs/keys>
STRIPE_WEBHOOK_SECRET=<https://stripe.com/docs/webhooks>
```
#### *Cоздайте и примените миграции (python3 для Mac):*
```
python manage.py makemigrations
python manage.py migrate
```

#### Заполните базу тестовыми данными (по желанию):

```
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/books.json
```
#### Запустите сервер
```
python manage.py runserver
```
#### Запустить [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```
   redis-server
   ```
   
#### Запустить Celery:
   ```
   celery -A store worker --loglevel=INFO
   ```
</details>

### Что могут делать пользователи на сайте:

**Авторизованные** пользователи могут:
1. Просматривать, страницу со всеми товарами и с отдельным товаром;
2. Просматривать, страницу с отдельной категорией товаров;
3. Заходить в свой профиль *(редактировать свои данные)*;
4. Добавлять и удалять товары из корзины;
5. Создавать заказы и оплачивать их

***Примечание***: Доступ ко всем операциям доступны только после аутентификации и авторизации.

**Неавторизованные** пользователи могут:
1. Просматривать, страницу со всеми товарами или отдельную страницу товара;
2. Просматривать, страницу с отдельной категорией товаров;
3. Авторизоваться;
4. Регистрироваться;
