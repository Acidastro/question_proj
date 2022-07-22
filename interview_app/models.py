from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Создать ответ. Привязать к вопросу
class Answer(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer_text = models.CharField(max_length=255, verbose_name='Текст ответа')

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Список ответов'

    # Получить количество опросов
    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return f"{self.answer_text[:25]}"


# Создать вопрос
class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель опроса', default='admin')
    text = models.TextField(verbose_name='Текст опроса')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    active = models.BooleanField(default=True, verbose_name='Активно')
    answer = models.ManyToManyField(Answer)

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Список тестов'

    # Проверка на повторное голосование
    def user_can_vote(self, user):
        """
        Вернет False если пользователь уже голосовал.
        Проверяет прикреплен ли опрос к данному пользователю
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(question=self)
        if qs.exists():  # если опрос не отвечен
            return False
        return True

    # Получить количество опросов
    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.text[:15]


# Создать выбор. Связать с пользователем, с вопросом и его ответом.
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Итоги опроса'
        verbose_name_plural = 'Итоги опроса'

    def __str__(self):
        return f'{self.question.text[:15]} - {self.answer.answer_text[:15]} - {self.user.login}'
