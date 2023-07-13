from datetime import timedelta

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import  get_user_model
from allauth.account.views import SignupView
from django.contrib.auth import login
from django.utils import timezone

from common.models import Member
from coupon.models import Coupon
from django.conf import settings

# 회원 가입

def detail(request, id):
    user = get_user_model()
    user = get_object_or_404(user, id=id)
    context = {
        'user': user
    }

    return render(request, 'common/detail.html', context)



class CustomSignupView(SignupView):
    def form_valid(self, form):
        # 회원가입 폼이 유효할 경우 회원가입 처리
        response = super().form_valid(form)
        # 회원가입한 사용자를 자동으로 로그인 처리
        login(self.request, self.user)

        # 이메일 보내기
        subject = '회원가입 축하 메일'
        message = '회원가입을 축하합니다!'

        from_email = settings.EMAIL_HOST_USER
        to_email = [self.user.email]  # 회원의 이메일 주소
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        #회원가입시 쿠폰 발급
        import random

        def code_random():
            # 8자리 랜덤 숫자 생성
            import string
            coupon_code = ''.join(random.choices(string.digits, k=8))
            return coupon_code
        now = timezone.now()
        coupon_code =code_random()
        coupon = Coupon.objects.create(code=str(coupon_code), active=True, use_from=now,
                                       use_to=now + timedelta(days=90), discount=10000, coupon_name="회원가입축하쿠폰")
        if coupon:
            member= Member.objects.create(
                email=self.user,
                coupon= coupon
                 )
            member.save()
            from django.contrib import messages
            message = f"회원가입을 축하합니다! 쿠폰 번호: {coupon.code}"
            messages.success(self.request, message)

        return redirect('/')




#쿠폰과 맴버 연결
def member_detail(request, coupon_code):
    member = Member.objects.get(code=coupon_code)


    context ={ 'member': member}
    return render(request, 'common/member_detail.html', context)

def membership(request):
    member = Member.objects.all()

    return render(request, 'common/membership.html', {'member': member})