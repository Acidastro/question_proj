from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.register, name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-list/', views.UserListView.as_view(), name='user-list'),
    path('color-list/', views.detail_color, name='color-list'),
    # path('test-color/', views.detail_color, name='test-color'),
    path('color-vote/', views.got_color, name='color-vote'),

]
