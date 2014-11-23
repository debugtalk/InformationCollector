#encoding=utf-8
from django import forms
from models import *
from django.forms import ModelForm


class BasicInfoForm(ModelForm):
    '''RecordPage2: ShopName, ShopType, ShopDetailAddress, IsChainShop'''
    class Meta:
        model = ShopInfo
        fields = ['ShopName', 'ShopType', 'ShopDetailAddress', 'IsChainShop']

class MacAddressInfoForm(ModelForm):
    '''RecordPage3: MacAddressList(one or many)'''
    class Meta:
        model = MacAddressInfo

class ContactInfoForm(ModelForm):
    '''RecordPage4: ContactInfoList(one or many)'''
    class Meta:
        model = ContactInfo

class ChainShopInfoForm(ModelForm):
    '''RecordPage5(if IsChainShop): ChainStoreInfo'''
    class Meta:
        model = ChainStoreInfo

# 商家信息的录入分多个页面
# Todo: merge step1 and step2
'''
RecordPage1: ShopDistrict
RecordPage2: ShopName, ShopType, ShopDetailAddress, IsChainShop
RecordPage3: MacAddressList(one or many)
RecordPage4: ContactInfoList(one or many)
RecordPage5(if IsChainShop): ChainStoreInfo
'''
