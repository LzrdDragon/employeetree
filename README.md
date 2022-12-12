<h1 align="center">Здравствуйте, меня зовут <a href="https://krasnoyarsk.hh.ru/applicant/resumes/view?resume=b609b18aff0b2682a10039ed1f38764d654268" target="_blank">Дмитрий</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/>
<p align="center">
<a href="https://github.com/LzrdDragon/employeetree"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&center=true&vCenter=true&width=435&lines=%D0%AD%D1%82%D0%BE+%D0%BC%D0%BE%D1%91+%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5+%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5" alt="Typing SVG" /></a>
</p>
</h1>

<h3 align="center">
    Древовидная структура подразделений компании с выводом сотрудников
</h3>
<p font-size="6" align="center">Ссылка на задание: https://docs.google.com/document/d/1mbZvp7GbTknanOjKF9IrPB7Zu4-tBnOHf09__HBLkqs/edit</p>

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

Переместитесь в дерикторию с manage.py
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
4. Создадим супер юзера (воспользуемся кастомной командой)
```bash
python manage.py initadmin --user=admin --password=password --force=True
```
<p align="right">Флаг "--force=True" говорит создать нам супер юзера, даже если он уже существует</p><br>
5. Запускаем проект
```bash
python manage.py runserver
```


</div>

<h1>
    Описание
</h1>

<b>Основной язык программирования</b><a href="#">:</a> Python 3.10.4<br>
<b>Framework</b><a href="#">:</a>  Django 4.1.2<br>
<br>
<b>Язык на Frontend'е</b><a href="#">:</a>  JavaScript<br>
<b>С использоваинем</b><a href="#">:</a>  jquery в качестве AJAX framework'а для асинхронных запросов к бэку<br>
<b>Web Framework</b>: Bootstrap<br>
<br>
<b>База данных</b><a href="#">:</a> PostgreSQL 14<br>



Структура проекта классическая, за исключением того, что я добавил модуль services.py для логики, которую хочется вынести из views.py, но не хочется добавлять в models.py, чтобы не "раздувать" модели и не было проблем с кольцевым импортом.

<h3>Из интересного</h3>
При открытии URL рендерится только структура подразделений, их конечно может быть много, но не миллионы, да и тысячи вряд ли, так что это должно работать быстро<br>
<br>
Если в подразделении есть сотрудники, то при открытия подразделения высвечивается кнопка "Показать сотрудников", при нажатии на которую, отправляется AJAX запрос на бэк с помощью jquery, распаршивается и выводится список сотрудников. Запрос отправляется только в том случае, если это первое нажатие на кнопку, далее сворачивается и разворачивается уже отрендеренный html<br>
<br>
В админке добавлено множество разных фильтров, полей поиска и можно выбрать тему<br>
<br>
Ограничения старался имплементировать на уровне модели, чтобы точно нельзя было записать в базу ошибочные данные

### Основные директории проекта

    .
    │   
    ├───Django-4.1.2.dist-info
    ├───django_admin_interface-0.22.1.dist-info
    ├───django_colorfield-0.7.2.dist-info
    ├───django_environ-0.9.0.dist-info
    ├───django_flat_responsive-2.0.dist-info
    ├───django_flat_theme-1.1.4.dist-info

