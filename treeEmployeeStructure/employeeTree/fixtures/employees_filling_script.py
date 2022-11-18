from ..models import Position, Division, Employee

all_divisions = Division.objects.exclude(id=1)
dev = Position.objects.get(id=1)
not_dev = Position.objects.get(id=2)

for division in all_divisions:
    if division.id != 2:
        for i in range(2000):
            Employee.objects.create(
                surname="Иванов",
                name="Иван",
                middle_name="Иванович",
                position=not_dev,
                division=division,
                salary=120000
            )
    else:
        for i in range(2000):
            Employee.objects.create(
                surname="Авдеев",
                name="Дмитрий",
                middle_name="Игоревич",
                position=dev,
                division=division,
                salary=120000
            )
