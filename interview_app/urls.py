from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_questions, name='list_questions'),
    path('<int:question_id>/', views.detail_question, name='detail_question'),
    path('<int:question_id>/vote/', views.question_vote, name='vote'),
]
