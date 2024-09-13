from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'photo']
    
        #fields = ('first_name','last_name','email','mobile','date_of_birth')
        #lables = {
        #    'first_name':'First Name'
        #}

        photo = forms.ImageField(
            label='Profile Picture',
            required=False,  # Make photo optional since default image is used
            widget=forms.FileInput(attrs={'class': 'custom-file-input'})
        )
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs )
        #self.fields('first_name').required = False
