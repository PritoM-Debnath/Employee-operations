from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Using HTML5 date picker
        }
        #fields = ('first_name','last_name','email','mobile','date_of_birth')
        #lables = {
        #    'first_name':'First Name'
        #}

        photo = forms.ImageField(
            label='Profile Picture',
            required=False,  
            widget=forms.FileInput(attrs={'class': 'custom-file-input'})
        )
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs )
        #self.fields('first_name').required = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
