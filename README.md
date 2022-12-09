<h1 align="center">Здравствуйте, меня зовут <a href="https://krasnoyarsk.hh.ru/applicant/resumes/view?resume=b609b18aff0b2682a10039ed1f38764d654268" target="_blank">Дмитрий</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/>
<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&center=true&vCenter=true&width=435&lines=%D0%AD%D1%82%D0%BE+%D0%BC%D0%BE%D1%91+%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5+%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5" alt="Typing SVG" /></a>
</p>
</h1>

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

</div>

<h1>
    Описание
</h1>

<span font-color="0">Main Programming Language</span><span>:</span><span> Python 3.10.4</span><br>
Also I used a little bit of: JavaScript<br>
With AJAX framowork for Asynchronous requests<br>
Database: PostgreSQL<br>
Front: Bootstrap<br>
Main Framework: Django 4.1.2<br>

Структура проекта классическая, за исключением того, что я добавил модуль services.py для логики, которую хочется вынести из views.py, но не хочется добавлять в models.py, чтобы не "раздувать" модели и не было проблем с кольцевым импортом

### A typical top-level directory layout

    .
    ├── build                   # Compiled files (alternatively `dist`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md

