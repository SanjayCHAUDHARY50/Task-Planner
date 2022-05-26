from dataclasses import field
from django import forms
from todolist_app.models import TaskList, Contact

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'sub', 'query']