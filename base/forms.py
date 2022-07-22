from django import forms
from .models import MyUser
from django.core.exceptions import ValidationError
from .models import UserColor


# Форма создания пользователя
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('login',)
        labels = {  # прописываем названия полей
            'login': 'Логин',
            'password': 'Пароль',
        }

    def clean_password2(self):
        # Проверка совпадения паролей
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Форма покупки цвета
class ColorBuyForm(forms.ModelForm):
    color = forms.CharField(label='Choice 1', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = UserColor
        fields = [
            'color',
            'color_price',
        ]
