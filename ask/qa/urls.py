from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('login/', auth_views.LoginView.as_view(
        template_name = 'qa/login.html',
    ), name='login'),
    path('signup/', views.user_creation, name='signup'),
    path('question/<int:question_id>/', views.question, name='question_id'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.test, name='new')
]