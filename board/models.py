
from django.db import models
from common.models import User
from item.models import Item


# 질문 모듈(q&n)
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject
# 답변 모듈(q&n)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content
# 공지사항 모듈(q&n)

class Notice(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    file = models.FileField(blank=True)
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

