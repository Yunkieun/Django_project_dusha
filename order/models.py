from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from common.models import Member, User
from coupon.models import Coupon
from item.models import Item

class Order(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    realname = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)  # 상품 금액
    shipping_price = models.IntegerField(default=0)  # 배송비
    total_price = models.IntegerField(default=0)  # 총 결제 금액
    created = models.DateTimeField(auto_now_add=True)
    #쿠폰 연결
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT, related_name='order_coupon', null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000000)])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_product(self):
        return sum(item.get_item_price() for item in self.items.all())

    def get_total_price(self):
        total_product = self.get_total_product()
        return total_product - self.discount

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.pk)

    def get_item_price(self):
        return self.price  *  self.quantity