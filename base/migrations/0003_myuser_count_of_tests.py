# Generated by Django 4.0.4 on 2022-07-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_myuser_date_of_birth_remove_myuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='count_of_tests',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество пройденных тестов'),
        ),
    ]
