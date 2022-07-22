from django.contrib import admin
from .models import Question, Answer, Vote


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "pub_date", "active"]
    search_fields = ["text"]
    list_filter = ["active"]
    filter_horizontal = ['answer']
    date_hierarchy = "pub_date"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text", ]
    search_fields = ["answer_text", ]


# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ["answer", "question", "user"]
#     search_fields = ["answer__answer_text", "question__text", "user__username"]
#     # autocomplete_fields = ["answer", "question", "user"]
