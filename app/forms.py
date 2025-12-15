from django import forms
from app.models import Voter_model

class Voter_form(forms.ModelForm):
    class Meta:
        model = Voter_model
        fields = ['name','father_name','dob','age','gender','address','Photo']
