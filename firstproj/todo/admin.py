from django.contrib import admin
from .models import user_todo, User
# Register your models here.

admin.site.register(user_todo)
admin.site.register(User)
