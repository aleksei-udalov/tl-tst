from collections import defaultdict

from django.http import JsonResponse
from django.shortcuts import render

from .models import Department, Employee


def index(request):
    return render(request, "employees/tree.html")


def departments(request):
    children = defaultdict(list)
    for dep in Department.objects.all():
        children[dep.parent_department.id if dep.parent_department else None].append(dep)

    def make_tree(dep_id):
        res = []
        for dep in children[dep_id]:
            res.append({
                'text': dep.name,
                'id': f'department_{str(dep.id)}',
                'nodes': make_tree(dep.id),
            })
        return res

    return JsonResponse({'departments': make_tree(None)})


def employees(request, department_id):
    empls = Employee.objects.filter(department__pk=department_id)
    return JsonResponse({
        'total': len(empls),
        'rows': [{
            'id': empl.id,
            'name': str(empl),
            'position': empl.position,
            'salary': empl.salary,
            'employment_date': empl.employment_date,
        } for empl in empls],
    })
