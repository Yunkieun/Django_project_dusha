from django.conf import settings

from coupon.models import Coupon
from item.models import Item

from decimal import Decimal


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            # 세션에 없던 키 값을 생성하면 자동 저장
            cart = self.session[settings.CART_ID] = {}
            # 세션에 이미 있는 키 값에 대한 값을 수정하면 수동으로 저장
        self.cart = cart
            # 쿠폰을 사용 할 수 있도록 세션에서 쿠폰 가져오기
        self.coupon_id = self.session.get('coupon_id')

    def __len__(self):
        # 요소가 몇개인지 갯수를 반환해주는 함수
        return sum(cart_item['quantity'] for cart_item in self.cart.values())


    def __iter__(self):
        # for문 같은 문법을 사용할 때 안에 있는 요소를 어떤 형태로 반환할 것인지 결정하는 함수
        Item_ids =   self.cart.keys()

        items = Item.objects.filter(id__in=Item_ids)

        for item in items:
            self.cart[str(item.id)]['item'] = item

        for cart_item in self.cart.values():
            cart_item['itme_price'] = Decimal(cart_item['item_price'])
            cart_item['total_price'] = Decimal( cart_item['item_price']) * cart_item['quantity']

            yield cart_item

    def add(self, item, quantity=1, is_update=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity':0, 'item_price':str(item.item_price)}
        # 만약 제품 정보가 Decimal 이라면 세션에 저장할 때는 str로 형변환 해서 저장하고
        # 꺼내올 때는 Decimal로 형변환해서 사용해야 한다.
        if is_update:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del(self.cart[item_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        # 장바구니를 비웠을 때 쿠폰도 삭제
        self.session['coupon_id'] = None
        self.session.modified = True

    #전체 제품 가격
    def get_product_total(self):
        return sum(Decimal(cart_item['item_price']) * cart_item['quantity'] for cart_item in self.cart.values())


    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)  # 데이터 베이스에서 쿠폰 가져오기

    # 할인 금액
    def get_discount_total(self):
        if self.coupon:
            if self.get_product_total() >= self.coupon.discount:
                return self.coupon.discount
        return Decimal(0)

    # 할인 금액이 반영된 상품 금액
    def get_total_price(self):
        return self.get_product_total() - self.get_discount_total()

