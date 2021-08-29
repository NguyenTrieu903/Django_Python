from django import forms
from django.forms import fields
from django.urls.base import clear_script_prefix
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from employee_register import models


class EmployeeForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullName', 'emp_code', 'mobile', 'position')
        labels = {
            'fullName': 'Full Name',
            'emp_code': 'EMP_Code'
        }

    def __init__(self, *args, **kwarges):
        super(EmployeeForm, self).__init__(*args, **kwarges)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
