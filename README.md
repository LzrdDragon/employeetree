# employeetree
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
