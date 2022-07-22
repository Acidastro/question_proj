from .models import Question
from django import forms


# Форма Опроса
class QuestionForm(forms.ModelForm):
    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control', }))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = Question
        fields = ['text', 'choice1', 'choice2',]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'cols': 20}),
        }

