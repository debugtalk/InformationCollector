#encoding:utf-8
from django.db import models

# Create your models here.

class MacAddressInfo(models.Model):
    mac_address = models.CharField(max_length = 48, unique=True, verbose_name=u'Mac地址')

    def __unicode__(self):
        return self.mac_address

    class Meta:
        verbose_name = u'Mac地址'
        verbose_name_plural = u'Mac地址列表'

class DistrictInfo(models.Model):
    province = models.CharField(max_length = 10, verbose_name = u'省份')
    city = models.CharField(max_length = 10, verbose_name = u'城市')
    county = models.CharField(max_length = 10, verbose_name = u'区／县')

    def __unicode__(self):
        return u"%s, %s, %s" % (self.province, self.city, self.county)

    class Meta:
        verbose_name = u'商家所在地区'
        verbose_name_plural = u'地区列表'

class ShopType(models.Model):
    shop_type = models.CharField(max_length = 10, unique=True, verbose_name=u'商家类型')

    def __unicode__(self):
        return self.shop_type

    class Meta:
        verbose_name = u'商家类型'
        verbose_name_plural = u'商家类型列表'

class ContactInfo(models.Model):
    name = models.CharField(max_length = 10, verbose_name=u'联系人姓名')
    duty = models.CharField(max_length = 10, verbose_name=u'联系人职务')
    phone = models.CharField(max_length = 15, verbose_name=u'联系人电话')
    email = models.EmailField(max_length = 20, verbose_name=u'电子邮箱')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'联系人信息'
        verbose_name_plural = u'联系人信息列表'

class ChainStoreInfo(models.Model):
    store_name = models.CharField(max_length = 10, verbose_name=u'连锁店名称')
    store_adress = models.CharField(max_length = 30, verbose_name=u'连锁店地址')
    contact_name = models.CharField(max_length = 10, verbose_name=u'连锁店联系人姓名')
    contact_phone = models.CharField(max_length = 13, verbose_name=u'连锁店联系人电话')

    def __unicode__(self):
        return self.store_name

    class Meta:
        verbose_name = u'连锁店信息'
        verbose_name_plural = u'连锁店信息列表'

class ShopInfo(models.Model):
    shop_name = models.CharField(max_length=20, unique=True, verbose_name=u'商家名称')
    mac_address_list = models.ManyToManyField(MacAddressInfo, verbose_name=u'Mac地址')
    shop_district = models.ForeignKey(DistrictInfo, verbose_name=u'商家所在地区')
    shop_address = models.CharField(max_length = 100, verbose_name=u'详细地址')
    shop_type = models.ForeignKey(ShopType, verbose_name=u'商家类型')
    contact_info_list = models.ManyToManyField(ContactInfo, verbose_name=u'商家联系人信息')
    is_chain_shop = models.BooleanField(default=False, verbose_name=u'是否连锁')
    chain_store_info = models.ForeignKey(ChainStoreInfo, blank=True, null=True, verbose_name=u'连锁店信息(若非连锁，请置空)')

    def __unicode__(self):
        return self.shop_name

    class Meta:
        verbose_name = u'商家信息'
        verbose_name_plural = u'商家信息列表'
