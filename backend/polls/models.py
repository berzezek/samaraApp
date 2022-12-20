from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_true = models.BooleanField(default=True)

    def __str__(self):
        return self.choice_text


class UsersTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.choice.choice_text}'
