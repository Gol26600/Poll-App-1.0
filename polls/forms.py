from django import forms
from .models import *


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option1', 'option2', 'option3', 'option4']

        widgets = {
            'question': forms.TextInput(attrs={'style': 'width: 80%'})
            }
