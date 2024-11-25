from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border-2 border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter the task title...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border-2 border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter the task description...',
                'rows': 4,
            }),
        }
