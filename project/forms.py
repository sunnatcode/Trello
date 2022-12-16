from django import forms

from project.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Project'}),
            'deadline': forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M']),
        }
