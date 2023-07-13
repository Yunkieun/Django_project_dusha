from django.contrib import admin

from coupon.models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_from', 'use_to', 'discount', 'active']
    list_filter = ['active', 'use_from', 'use_to']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)