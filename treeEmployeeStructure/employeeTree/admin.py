from django.contrib import admin

from .models import Division, Position, Employee
from .forms import DivisionModelForm, PositionModelForm, EmployeeModelForm
from .services import custom_titled_filter


class DivisionAdmin(admin.ModelAdmin):
    form = DivisionModelForm
    search_fields = ['name', 'parent__name', 'level']
    list_filter = (
        ("parent", custom_titled_filter('Находится в иерархии под')),
    )
    fieldsets = (
        ('Информация о подразделении', {
            'fields': ('name', ),
            'description': 'Общая информация'
        }),
        ('Иерархия', {
            'fields': ('parent',),
            'description': 'Выберите главенствующее подразделение'
        }),
    )


class PositionAdmin(admin.ModelAdmin):
    form = PositionModelForm
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': ('name',),
            'description': 'Добавьте должность 1 раз и выбирайте её из списка при добавлении сотрудников'
        }),
    )


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeModelForm
    search_fields = [
        'name',
        "surname",
        "middle_name",
        "employed_date",
        "division__name",
        "position__name",
        'salary'
    ]
    list_filter = (
        ("employed_date", custom_titled_filter('Дата трудоустройства')),
        ("division", custom_titled_filter('Подразделение')),
        ("position__name", custom_titled_filter('Должность')),
        ('salary', custom_titled_filter('Зарплата'))
    )
    fieldsets = (
        ('Фамилия Имя Отчество', {
            'fields': ('name', 'surname', 'middle_name'),
            'description': 'Если отчества нет, оставьте это поле пустым'
        }),
        ('Информация о подразделении, заработной плате и дате трудоустройства', {
            'fields': ('employed_date', 'division', 'position', 'salary'),
            'description': 'Если оставить дату трудоустройства незаполненной, автоматически будет '
                           'сохранена сегодняшняя дата'
        }),
    )


admin.site.register(Division, DivisionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
