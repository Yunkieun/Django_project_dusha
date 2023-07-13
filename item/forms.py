from django import forms

from item.models import Item

#아이템 폼 생성
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item #아이템 객체 생성
        fields = ['item_title', 'content', 'item_price', 'item_image']