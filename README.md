<h1 align="center">Здравствуйте, меня зовут <a href="https://krasnoyarsk.hh.ru/applicant/resumes/view?resume=b609b18aff0b2682a10039ed1f38764d654268" target="_blank">Дмитрий</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/>
<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&center=true&vCenter=true&width=435&lines=%D0%AD%D1%82%D0%BE+%D0%BC%D0%BE%D1%91+%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5+%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5" alt="Typing SVG" /></a>
</p>
</h1>

<h3>
    Древовидная структура отделов компании с выводом сотрудников
</h3>
<span>Ссылка на задание: https://docs.google.com/document/d/1mbZvp7GbTknanOjKF9IrPB7Zu4-tBnOHf09__HBLkqs/edit</span>

<h1>
    Разворот проекта
</h1>

<div>
<h3>1. Docker</h3>
<span>Команда для разворота проекта:</span><br><br>

```bash
docker-compose up --build -d
```
или просто
```bash
docker-compose up --build
```
чтобы видеть логи

<span>Главная страница будет доступна по адресу: <a href="http://localhost/" target="_blank">localhost</a></span><br>
<span>Административная панель: <a href="http://localhost/admin/" target="_blank">localhost/admin/</a></span>

<h3>2. Классический через manage.py со своей базой</h3>
<span>Прежде всего необходимо создать базу и задать её параметры в файле ".env", который находится в одной дериктории с модулем "settings.py". Я использовал PostgreSQL, поэтому дефолтные настройки заданы для неё, точнее для Docker контейнера с ней.</span><br><br>

1. Создадим миграции (на всякий случай, они уже должны быть)
```bash
python manage.py makemigrations
```
2. Выполним миграции
```bash
python manage.py migrate
```
3. Соберём статические файлы
```bash
python manage.py collectstatic --noinput
```

<span>Главная страница будет доступна по адресу: <a href="http://localhost/" target="_blank">localhost</a></span><br>
<span>Административная панель: <a href="http://localhost/admin/" target="_blank">localhost/admin/</a></span>
</div>

<h1>
    Описание
</h1>

Основной язык программирования<a href="#">:</a> Python 3.10.4<br>
Framework<a href="#">:</a>  Django 4.1.2<br>
<br>
Язык на Frontend'е<a href="#">:</a>  JavaScript<br>
С использоваинем<a href="#">:</a>  jquery в качестве AJAX framework'а для асинхронных запросов к бэку<br>
и Bootstrap framework составления визкальной части дерева<br>
<br>
База данных<a href="#">:</a> PostgreSQL 14<br>


Структура проекта классическая, за исключением того, что я добавил модуль services.py для логики, которую хочется вынести из views.py, но не хочется добавлять в models.py, чтобы не "раздувать" модели и не было проблем с кольцевым импортом.

### A typical top-level directory layout

    .
    ├── build                   # Compiled files (alternatively `dist`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md
