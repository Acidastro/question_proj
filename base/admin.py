from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import MyUser, UserColor


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('login', 'password')

    def clean_password2(self):
        # Убедиться что две записи совпадают
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Сохранить пароль
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('login', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('login', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal info', {'fields': ('login',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    )
    search_fields = ('login',)
    ordering = ('login',)
    filter_horizontal = ()


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['login', 'chain', 'user_color']


@admin.register(UserColor)
class MyUserColorAdmin(admin.ModelAdmin):
    list_display = ['color', 'color_price']
