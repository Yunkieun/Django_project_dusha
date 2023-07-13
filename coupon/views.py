from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from common.models import Member
from coupon.forms import AddCouponForm
from coupon.models import Coupon
from order.models import Order


#쿠폰 추가
@login_required(login_url='/member/login/')
def add_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)


    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now, use_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist as e:
            request.session['coupon_id'] = None
    return redirect('cart:detail')



# 맴버쉽 설정
@login_required(login_url='/login/')
def grade(request):
    member_info = Member.objects.all()
    orders = Order.objects.filter(user_id=request.user)
    total = sum([order.total_price for order in orders])
    if total > 1000000:
        member_info.user_grade = 'mvp'
        member_info.coupon = '30%'
    elif total > 500000:
        member_info.user_grade = 'platinum'
        member_info.coupon = '20%'
    else:
        member_info.user_grade = 'normal'
        member_info.coupon = '10%'
    context = {
        'total': total,
        ' member_info': member_info
    }
    return render(request, 'common/profile-rate.html', context)
