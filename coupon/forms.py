from django import forms

from django.contrib.auth.models import User


class AddCouponForm(forms.Form):
    code = forms.CharField(label="coupon code")

