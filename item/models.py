from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse

from config import settings


# 카테고리 모델
class Category(models.Model):
    # unique=True 중복 불허
    name = models.CharField(max_length=50, unique=True, db_index=True)
    # url주소 - 문자, allow_unicode - 한글허용
    slug = models.SlugField(max_length=200, unique=True,
                            allow_unicode=True, db_index=True)

    def __str__(self):
        return self.name

    # 카테고리 url 주소
    def get_absolute_url(self):

        return reverse('item:category_page', args=[self.slug])

    # 관리자 페이지에서 적용 - verbose_name_plural(복수형)
    class Meta:
        ordering = ['name']  # 이름순 정렬
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Item(models.Model):
    # 상품 번호, 상품명, 상품가격, 카테고리번호, 출시일, 판매량, 상품사진 , 총재고량

    GENDER_CHOICES = (
        ('MEN', 'MEN'),
        ('WOMEN', 'WOMEN'),
    )
    id = models.AutoField(primary_key=True, db_index=True)
    item_category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    item_title = models.CharField(max_length=100, unique=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=1)
    content = models.TextField()
    item_price = models.IntegerField()
    # 아이템 카테고리에 속한 상품이 존재하면 카테고리 삭제 불가
    # 재고가 있으면 false 재고가 없으면 true
    soldout = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    item_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='item_likes', blank=True)
    item_image = models.ImageField(upload_to="item/item_img/%Y/%m/%d") #제품 메인사진
    sales = models.IntegerField(default=0) #판매량
    item_content = models.ImageField(upload_to='item/item_content/%Y/%m/%d') #제품 상세 사진
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.item_title

    def category_name(self):
        return self.item_category

    def get_absolute_url(self):
        return reverse('item:item_detail', args=[self.id])

    class Meta:
        ordering = ['-create_date', 'id']  # 작성일순 정렬
        index_together = [['id']]





