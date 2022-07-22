# Generated by Django 4.0.4 on 2022-07-20 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview_app', '0004_answer_alter_question_options_alter_vote_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель опроса'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.answer', verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.PositiveIntegerField(default=0, verbose_name='Монеты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
