import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    # fields will be stored in the database
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "Question: {}, Date Published: {}".format(self.question_text, self.pub_date)

    def was_published_recently(self):
        time_diff = 1

        return self.pub_date >= timezone.now() - datetime.timedelta(days=time_diff) and self.pub_date < timezone.now()


class Choice(models.Model):
    # idk what foreign key means
    # foreign key = each Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "Choice Text: {}, Votes: {}".format(self.choice_text, self.votes)
