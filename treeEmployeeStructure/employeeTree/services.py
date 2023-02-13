from __future__ import annotations
from abc import ABC
from typing import Iterable, Generator

from django.contrib import admin

from .models import Division, Employee


def custom_titled_filter(title: str | None = None):
    """
    Allows to add a custom names for filtering tags

        Changing a title of a filtering object to the given title at the moment of its initialization
    """

    if title is not None:

        class Wrapper(admin.FieldListFilter, ABC):
            def __new__(cls, *args, **kwargs):
                instance = admin.FieldListFilter.create(*args, **kwargs)
                instance.title = title
                return instance

        return Wrapper
    else:
        print("Tittle argument is necessary")


class DivisionAggregation:
    @staticmethod
    def find_a_parent(
        division: Division | None = None, where_to_search: dict | None = None
    ) -> dict | None:
        """
        Recursively finds a dict which contains a division as a key, if exists and returns it, else
        returns None
        """

        # check for attributes
        if division and where_to_search is not None:
            # validate attributes
            if not isinstance(where_to_search, dict):
                raise AttributeError(
                    '"find_a_parent()" expects dict as a second argument.'
                )
            if not isinstance(division, Division):
                raise AttributeError(
                    '"find_a_parent()" expects an instance of a Division model '
                    "class as a first argument."
                )

            # find a parent dict
            if division in where_to_search.keys():
                return where_to_search
            for value in where_to_search.values():
                if value["subdivisions"]:
                    parent_dict = DivisionAggregation.find_a_parent(
                        division, value["subdivisions"]
                    )
                    if parent_dict:
                        return parent_dict
            return None

        else:
            raise AttributeError('"find_a_parent()" expects 2 arguments.')

    @staticmethod
    def get_main_divisions_tree() -> dict:
        """
        Returns all divisions, which are don't have parents as a dictionary,
        which looks like:

        {
            division_0: {
                'employees': [],
                'subdivisions': {}
            }

                ...

            division_n: {
                'employees': [],
                'subdivisions': {}
            }
        }
        """
        divisions_tree = {}
        main_divisions = Division.objects.filter(parent=None)
        employees = main_divisions.prefetch_related("employee_set")
        for division in main_divisions:
            division_employees = employees.filter(division=division)
            if division_employees:
                divisions_tree[division] = {"employees": True, "subdivisions": {}}
            else:
                divisions_tree[division] = {"employees": False, "subdivisions": {}}
        return divisions_tree

    @staticmethod
    def make_subdivisions_dicts(subdivisions: Iterable[Division]) -> Generator:
        """Creates for each given division a dictionary which has the division as a key
        and a {'employees': [], 'subdivisions': {}} dictionary as a value and yields both of it,
        as division, as a dictionary.
            It's designed to be used in loops
        """
        for division in subdivisions:
            division_employees = Employee.objects.filter(division=division)

            if division_employees:
                subdivision_tree = {division: {"employees": True, "subdivisions": {}}}
            else:
                subdivision_tree = {division: {"employees": False, "subdivisions": {}}}

            yield division, subdivision_tree


def get_employees_dict(employees_container: Iterable[Employee]) -> dict:
    """Creates and returns a JSONish dictionary with ids of employee and its data as a nested dictionary to send it
    to a Frontend"""
    employees_dict = {}
    for employee in employees_container:
        employees_dict[str(employee.pk)] = {
            "surname": str(employee.surname),
            "name": str(employee.name),
            "middle_name": str(employee.middle_name),
            "employed_date": str(employee.employed_date),
            "position": str(employee.position.name),
            "salary": str(employee.salary),
        }
    return employees_dict
