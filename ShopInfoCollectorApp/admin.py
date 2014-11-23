#encoding:utf-8
from django.contrib import admin

# Register your models here.
from ShopInfoCollectorApp.models import MacAddressInfo, DistrictInfo, ShopType, ContactInfo, ChainStoreInfo, ShopInfo
from ShopInfoCollectorApp.models import DistrictInfo, Province, City, County


class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ShopName', 'ShopDistrict', 'ShopDetailAddress', 'ShopType')
    list_filter = ['ShopName']
    search_fields = ['ShopName',]
    list_per_page = 20

admin.site.register(MacAddressInfo)
admin.site.register(ShopType)
admin.site.register(ContactInfo)
admin.site.register(ChainStoreInfo)
admin.site.register(DistrictInfo)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(County)
admin.site.register(ShopInfo, ShopInfoAdmin)
