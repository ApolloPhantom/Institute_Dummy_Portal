from django import forms
from .models import Faculty, Alumni

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'email', 'department', 'designation', 
                 'joining_date', 'bio', 'image']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name', 'email', 'graduation_year', 'degree',
                 'current_company', 'position', 'linkedin_profile', 'image']
        widgets = {
            'graduation_year': forms.NumberInput(attrs={'min': 1900, 'max': 2024}),
        }