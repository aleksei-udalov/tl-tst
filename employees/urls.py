from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments', views.departments, name='departments'),
    path('employees_by_department/<int:department_id>', views.employees, name='employees'),
]
