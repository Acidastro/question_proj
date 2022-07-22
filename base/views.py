from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import MyUser, UserColor
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "base/home.html")


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
            return render(request, 'base/home.html', {'new_user': new_user})
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})


class UserListView(ListView):
    template_name = 'base/list_users.html'
    model = MyUser
    context_object_name = 'users'

    def get_queryset(self):  # можно создать сортировку
        queryset = super().get_queryset()
        filter_qs = queryset.order_by('-count_of_tests', 'login')  # принимаем записи с нужным фильтром
        return filter_qs


class ColorListView(ListView):
    template_name = 'base/test.html'
    model = UserColor
    context_object_name = 'colors'

    def get_queryset(self):  # можно создать сортировку
        queryset = super().get_queryset()
        filter_qs = queryset.order_by('-color_price', 'color')  # принимаем записи с нужным фильтром
        return filter_qs


# Страница опроса
def detail_color(request):
    colors = UserColor.objects.all()  # все объекты колор
    loop_count = colors.count()  # количество цветов
    context = {
        'colors': colors,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'base/list_color.html', context)


def got_color(request):
    color_id = request.POST.get('choice')
    user = MyUser.objects.get(login=request.user)
    color = UserColor.objects.get(id=color_id)
    if color_id:  # Выбор сделан. Сохранить
        if user.chain >= color.color_price:
            print(user.user_color, color.color)
            user.chain -= color.color_price
            user.user_color_id = color.id
            user.save()
        else:
            messages.error(request, 'Не хватает денег. Пройдите больше опросов!')
            return redirect('test-color')
        return redirect('home')
    else:  # Выбор не сделан

        return redirect("test-color")
