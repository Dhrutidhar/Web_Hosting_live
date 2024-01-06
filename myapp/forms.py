from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = '__all__'

class updateform(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = ['firstname', 'lastname', 'username', 'password', 'city', 'state', 'mobile']

class notesform(forms.ModelForm):
    class Meta:
        model = mynotes
        fields = '__all__'

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'