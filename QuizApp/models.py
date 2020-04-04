from django.db import models

# Create your models here.

class Quiz(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):

    description = models.CharField(max_length=10000)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_option = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.description

class Answer(models.Model):

    option = models.CharField(max_length=1, unique=False)
    description = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.description
