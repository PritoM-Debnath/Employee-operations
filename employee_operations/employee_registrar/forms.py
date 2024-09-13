from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ('first_name','last_name','email','mobile','date_of_birth')
        #lables = {
        #    'first_name':'First Name'
        #}

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs )
        #self.fields('first_name').required = False
