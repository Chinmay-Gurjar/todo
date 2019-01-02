from django.db import models

class User(models.Model) :
    username = models.CharField(max_length = 200, primary_key = True)
    def __str__(self):
        return self.username

class user_todo(models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 1000)
    date = models.DateTimeField('date published')
    flag = models.BooleanField(default = False)
    def __str__(self):
        return self.description
