from django.db import models

# Create your models here.

class Question(models.Model):
    objects = models.Manager()
    question_text = models.CharField(max_length=200)
    pub_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    #커스텀 메소드

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timelta(days=1)

class Choice(models.Model):
    objects = models.Manager()
    qusetion = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #참고하는 행의 행이  삭제되면 대응되는 행들도 같이 삭제됨 => 여기서는  Question의 행이 삭제되면 관련 행이 Choice에서도 삭제됨
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text