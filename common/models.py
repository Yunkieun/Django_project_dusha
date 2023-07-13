from django.db import models
# AbstractUser 사용
from django.contrib.auth.models import AbstractUser

from coupon.models import Coupon


# AbstractUser 상속받는 유저 클래스 생성
class User(AbstractUser):
    pass




class Member(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    nickname = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    birth = models.DateField(null=True)
    user_grade = models.CharField(default=0, max_length=50 ) # normal, platinum, mvp (3등급)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):

        return self.nickname

