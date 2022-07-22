from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import MyUser, UserColor
from django.contrib import messages
from django.contrib.auth import login as log, authenticate


class Home(TemplateView):
    template_name = 'base/home.html'


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            # Создать объект пользователя
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(user_form.cleaned_data['password1'])
            # Сохранить объект пользователя
            new_user.save()
            # Далее сразу выполнить вход!
            login = user_form.cleaned_data.get('login')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(request, login=login, password=password)
            if user:
                log(request, user)

            return render(request, 'base/home.html', {'new_user': new_user})
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})


class UserListView(ListView):
    template_name = 'base/list_users.html'
    model = MyUser
    context_object_name = 'members'

    def get_queryset(self):  # можно создать сортировку
        queryset = super().get_queryset()
        filter_qs = queryset.order_by('-count_of_tests', 'login')  # принимаем записи с нужным фильтром
        return filter_qs


def user_detail(request, user_id):
    member = MyUser.objects.get(id=user_id)
    return render(request, 'base/user_detail.html', {
        'member': member,
    })


# class UserDetailView(TemplateView):
#     template_name = 'base/user_detail.html'


class ColorListView(ListView):
    template_name = 'base/list_color.html'
    model = UserColor
    context_object_name = 'colors'

    def get_queryset(self):  # можно создать сортировку
        queryset = super().get_queryset()
        filter_qs = queryset.order_by('-color_price', 'color')  # принимаем записи с нужным фильтром
        return filter_qs


# Страница выбора цвета
def detail_color(request):
    colors = UserColor.objects.all()  # все объекты колор
    loop_count = colors.count()  # количество цветов
    context = {
        'colors': colors,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'base/list_color.html', context)


# Покупка цвета
def got_color(request):
    color_id = request.POST.get('choice')
    user = MyUser.objects.get(login=request.user)

    if color_id:  # Выбор сделан. Сохранить
        color = UserColor.objects.get(id=color_id)
        if user.chain >= color.color_price:
            user.chain -= color.color_price
            user.user_color_id = color.id
            user.save()
        else:
            messages.error(request, 'Не хватает денег. Пройдите больше опросов!')
            return redirect('color-list')
        return redirect('home')
    else:  # Выбор не сделан

        return redirect("color-list")
