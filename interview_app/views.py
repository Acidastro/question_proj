from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import Question, Answer, Vote
from django.contrib import messages


# Страница списка опросов
@login_required()  # проверка входа
def list_questions(request):
    all_questions = Question.objects.all()
    all_votes = Vote.objects.all()
    context = {
        'all_questions': all_questions,
    }
    return render(request, 'interview_app/list_questions.html', context)


# Страница опроса
def detail_question(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)

    if not question.active:  # Если опрос пройден, показать результат
        return render(request, 'interview_app/question_result.html', {'question': question})
    loop_count = question.answer_set.count()
    context = {
        'question': question,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'interview_app/question_detail.html', context)


# Страница прохождения опроса
@login_required
def question_vote(request, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    answer_id = request.POST.get('choice')
    user_can_vote = question.user_can_vote(request.user)

    if not user_can_vote:  # если опрос уже был пройден

        # ~~~~~~~вывести сообщение
        messages.error(request, 'Вы уже проходили этот опрос')
        return redirect("list_questions")

    if answer_id:  # Выбор сделан. Сохранить
        user = request.user
        user.chain += 1  # добавить монету
        user.count_of_tests += 1  # добавить пройденный тест
        user.save()
        answer = Answer.objects.get(id=answer_id)
        vote = Vote(user=request.user, question=question, answer=answer)
        vote.save()
        print(vote)
        return render(request, 'interview_app/question_result.html', {'question': question})
    else:  # Выбор не сделан

        return redirect("detail_question", question_id)
