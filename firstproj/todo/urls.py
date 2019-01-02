from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.MainPage, name = 'MainPage'),
    path('alltodo', views.AllTodos, name = 'AllTodo'),
    path('user/<slug:user_name>', views.Spec_todo, name = 'Spec_todo'),
    path('add_user', views.AddUser, name = 'AddUser'),
    path('add_todo', views.AddTodo, name = 'AddTodo'),
    path('thanks', views.ThankYouPage, name = 'ThankYouPage'),
    path('all_users', views.AllUser, name = 'AllUsers'),
]
