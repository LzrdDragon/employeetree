from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse

from .models import Division, Employee
from .services import DivisionAggregation, get_employees_dict


def index(request):

    divisions_tree = DivisionAggregation.get_main_divisions_tree()

    subdivisions = Division.objects.exclude(parent=None).order_by('parent')
    for division, subdivision_tree in DivisionAggregation.make_subdivisions_dicts(subdivisions):
        parent_dict = DivisionAggregation.find_a_parent(division.parent, divisions_tree)
        if parent_dict is not None:
            parent_dict[division.parent]['subdivisions'].update(subdivision_tree)

    context = {
        'base_page': 'base.html',
        'tree_template': 'tree.html',
        'header_template': 'header.html',
        'footer_template': 'footer.html',
        'divisions_tree': divisions_tree
    }

    return render(request, 'index.html', context=context)


def get_employees(request, division_id):
    if division_id is None:
        return HttpResponseBadRequest
    else:
        employees_list = Employee.get_division_employees(division_id=division_id, order='employed_date')
        employees_dict = get_employees_dict(employees_list)

    return JsonResponse(employees_dict)
