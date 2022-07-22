from django.contrib import admin
from .models import Question, Answer, Vote


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "owner", "pub_date", "active"]
    search_fields = ["text", "owner__username"]
    list_filter = ["active"]
    date_hierarchy = "pub_date"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text", "question"]
    search_fields = ["answer_text", "question__text"]
    autocomplete_fields = ["question"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["answer", "question", "user"]
    search_fields = ["answer__answer_text", "question__text", "user__username"]
    # autocomplete_fields = ["answer", "question", "user"]
