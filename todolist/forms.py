from django import forms
import datetime
from todolist.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoTask
        fields = ['task_title', 'task_description']
        
    
