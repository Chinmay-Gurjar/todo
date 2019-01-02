from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import user_todo, User
from .forms import AddUserForm, AddTodoForm
from django.utils import timezone
# Create your views here.

def MainPage(request) :
    form = AddUserForm()
    return render(request, 'todo/main_page.htm', {'form':form})

def AllTodos(request) :
    all_todos = user_todo.objects.order_by('-date')
    context = {'all_todo' : all_todos}
    return render(request, 'todo/Alltodo.htm', context)

def Spec_todo(request, user_name) :
    utodo = get_object_or_404(User, username = user_name)
    return render(request, 'todo/spec_todo.htm', {'utodo':utodo})

def AddUser(request) :
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            new_user = User(username = user_name)
            new_user.save()
            return HttpResponseRedirect('thanks')
    else:
        form = AddUserForm()
    return render(request, 'todo/add_user.htm', {'form':form})

def AddTodo(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            description = form.cleaned_data['description']
            dateTime = timezone.now()
            user_obj = User.objects.get(username = user )
            new_todo = user_todo(user = user_obj, description = description, date = dateTime)
            new_todo.save()
            return HttpResponseRedirect('thanks')
    else:
        form = AddTodoForm()
    return render(request, 'todo/add_todo.htm', {'form':form})

def ThankYouPage(request):
    return render(request, 'todo/thanks.htm')

def AllUser(request) :
    users_list = User.objects.all()
    return render(request, 'todo/all_user.htm', {'users_list':users_list})
