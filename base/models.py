from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserColor(models.Model):
    # green, black, white, red, blue,yellow, pink, cyan
    color = models.CharField(max_length=40, unique=True)
    color_price = models.IntegerField(null=True, default=0)

    @staticmethod
    def get_default_user_settings():
        user_color, created = UserColor.objects.get_or_create(color='white', color_price=0)
        return user_color

    def __str__(self):
        return self.color


class MyUserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError('Get login')

        user = self.model(
            login=login
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None):
        user = self.create_user(
            login=login,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    login = models.CharField(
        verbose_name='Логин',
        max_length=20,
        unique=True,
        null=True,
    )
    chain = models.PositiveIntegerField(default=0, verbose_name='Валюта')
    user_color = models.ForeignKey(UserColor, on_delete=models.CASCADE, null=True, verbose_name='Цвет')
    count_of_tests = models.PositiveIntegerField(default=0, verbose_name='Количество пройденных тестов')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # def save(self, *args, **kwargs):
    #     if self.user_color is None:
    #         self.user_color = UserColor.get_default_user_settings()
    #     super(MyUser, self).save(*args, **kwargs)
