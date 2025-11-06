from django import forms
from .models import Application

# Application Form:

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name','linkedin_url','location','phone','email','Experience',]
        labels = {
            "linkedin_url": "LinkedIn Profile URL"
        }

