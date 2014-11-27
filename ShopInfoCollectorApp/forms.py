#encoding=utf-8
from django import forms
from models import *
from django.forms import ModelForm

class BasicInfoForm(ModelForm):
    '''RecordPage1: ShopDistrict, ShopName, ShopType, ShopDetailAddress, IsChainShop'''
    class Meta:
        model = ShopInfo
        fields = ['shop_name', 'shop_type', 'shop_address', 'is_chain_shop']

class MacAddressInfoForm(ModelForm):
    '''RecordPage2: MacAddressList(one or many)'''
    class Meta:
        model = MacAddressInfo
        exclude = []

class ContactInfoForm(ModelForm):
    '''RecordPage3: ContactInfoList(one or many)'''
    class Meta:
        model = ContactInfo
        exclude = []

class ChainShopInfoForm(ModelForm):
    '''RecordPage4(if IsChainShop): ChainStoreInfo'''
    class Meta:
        model = ChainStoreInfo
        exclude = []

# 商家信息的录入分多个页面
'''
RecordPage1: ShopDistrict, ShopName, ShopType, ShopDetailAddress, IsChainShop
RecordPage2: MacAddressList(one or many)
RecordPage3: ContactInfoList(one or many)
RecordPage4(if IsChainShop): ChainStoreInfo
'''
