# Generated by Django 4.0.4 on 2022-07-21 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_usercolor_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='color',
            new_name='user_color',
        ),
    ]