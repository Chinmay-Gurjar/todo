from django import forms

class AddUserForm(forms.Form):
    username = forms.CharField(max_length = 200)

class AddTodoForm(forms.Form):
    user = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000)
