from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    file = models.FileField(blank=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Some(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True)
    qwe = models.IntegerField()


class SomeM2M(models.Model):
    question = models.ManyToManyField(Question)
