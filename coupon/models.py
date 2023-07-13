import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True )
    use_from = models.DateTimeField() #기간설정
    use_to = models.DateTimeField()   #기간설정
    coupon_name = models.CharField(max_length=50)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

