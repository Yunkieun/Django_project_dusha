from django import forms
from common.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nickname', 'phone', 'address', 'birth', 'user_grade', 'coupon']