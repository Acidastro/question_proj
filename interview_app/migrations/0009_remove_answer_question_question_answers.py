# Generated by Django 4.0.4 on 2022-07-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_app', '0008_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='interview_app.answer'),
        ),
    ]
