from django import forms
from django.core import validators
from .models import AddUser

class AddForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)
    # age = forms.IntegerField()
    class Meta:
        model = AddUser
        fields = ['name','email','age']
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
    