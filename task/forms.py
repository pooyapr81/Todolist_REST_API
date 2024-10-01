from .models import TodoTask
from django import forms


class DataInput(forms.DateInput):
    input_type = 'date'


class TaskCreateForm(forms.ModelForm):
    created = forms.DateField(widget=DataInput)

    class Meta:
        model = TodoTask
        fields = ('title', 'created', 'category')
