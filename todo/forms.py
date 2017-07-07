from django import forms
from .models import Task
from django.contrib import admin


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        creation_date = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        fields = ['title', 'description', 'status']

    def clean(self):
        if not self.cleaned_data.get('title') or not self.cleaned_data.get('description'):
            raise forms.ValidationError(
                "Please Fill all the fields"
            )


class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
