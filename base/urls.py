from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("signup/", views.register, name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-list/', views.UserListView.as_view(), name='user-list'),
    path('user-detail/<int:user_id>/', views.user_detail, name='user-detail'),
    path('color-list/', views.detail_color, name='color-list'),
    path('color-vote/', views.got_color, name='color-vote'),

]
