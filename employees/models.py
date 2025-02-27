from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Department name')
    parent_department = models.ForeignKey('Department', null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255)
    employment_date = models.DateField()
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname or ""}'
