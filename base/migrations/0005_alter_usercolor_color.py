# Generated by Django 4.0.4 on 2022-07-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_usercolor_myuser_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolor',
            name='color',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
