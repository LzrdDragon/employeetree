from django import forms

from .models import Division, Position, Employee


class DivisionModelForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ['name', 'parent']
        labels = {
            'name': 'Название подразделения',
            'parent': 'Главенствующее подразделение'
        }


class PositionModelForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['name']
        labels = {
            'name': 'Должность'
        }


class EmployeeModelForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['surname', 'name', 'middle_name', 'employed_date', 'position', 'division', 'salary']
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'middle_name': 'Отчество',
            'employed_date': 'Дата трудоустройства',
            'position': 'Должность',
            'division': 'Подразделение',
            'salary': 'Заработная плата'
        }
