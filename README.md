<h1 align="center">Hi there, I'm <a href="https://daniilshat.ru/" target="_blank">Daniil</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Computer science student, IT news writer from Russia 🇷🇺</h3>
Avdeev Test Task

Есть 2 варианта разворота проекта:
1. Docker
    Команда для разворота проекта:
      docker-compose up --build -d
    Главная страница доступна по адресу: http://localhost/
    Административная панель: http://localhost/admin/
2. Классический через manage.py со своей базой

Структура проекта классическая Джанговская. За исключением того, что я добавил модуль services.py и обернул всё в Docker для удобного разворота

Опишу здесь основные пункты по проекту

Database: PostgreSQL
Front: 
