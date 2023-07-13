from django import forms

from common.models import Member
from order.models import Order


#Order 폼 생성
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['realname', 'email', 'address', 'phone']



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nickname', 'phone', 'address', 'birth', 'user_grade', 'coupon']