## Проект по django "Запись на тестдрайв"
### Руководство пользователя.
Проект представляет собой сайт из трех страниц с функцией записи на тестдрайв.
На главной странице отображаются активные записи клиентов.
<img width="1061" height="515" alt="image" src="https://github.com/user-attachments/assets/6853c2d1-d0bc-4941-9fe5-839825936964" />

Вторая страница на которой находится информация о компании
<img width="1185" height="692" alt="image" src="https://github.com/user-attachments/assets/7f0ca55d-2795-4f84-ad81-e8cb5e8c3556" />

На третей странице под названием тестдрайв находится форма, при заполнение которой ваша запись появляется на главной странице
<img width="919" height="703" alt="image" src="https://github.com/user-attachments/assets/2e6bfdc1-6b24-4dc1-ad09-4bef10276bd8" />
###Руководство программиста.
>Django («Джанго») — свободный фреймворк для веб-приложений и сайтов на языке Python с открытым исходным кодом.

Начало работы со средой:
```

# Создаю вирт. среду
python -m venv .venv
# Активирую вирт. среду
.venv\Scripts\activate
# Усланавливаю библиотеку
pip install django==5
# Создаю проект
django-admin startproject testdrive
# Перехожу в папке проекта
cd testdrive
# Создаю приложение
python manage.py startapp myapp
#Перейдите в файл settings.py и в разделе INSTALLED_APPS впишите (в конце) название приложения "myapp"
# Запускаю проект
python manage.py runserver
