#encoding:utf-8
from django.db import models

# Create your models here.

class MacAddressInfo(models.Model):
    MacAddress = models.CharField(max_length = 48, unique=True, verbose_name=u'Mac地址')

    def __unicode__(self):
        return self.MacAddress

    class Meta:
        verbose_name = u'Mac地址'
        verbose_name_plural = u'Mac地址列表'

# District Info
class Province(models.Model):
    name = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length = 10)
    province = models.ForeignKey(Province, related_name = "cities")

    def __unicode__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length = 10)
    city = models.ForeignKey(City, related_name = "counties")

    def __unicode__(self):
        return self.name

class DistrictInfo(models.Model):
    province = models.ForeignKey(Province, verbose_name = u'省份')
    city = models.ForeignKey(City, verbose_name = u'城市')
    county = models.ForeignKey(County, verbose_name = u'区／县')

    def __unicode__(self):
        return u"%s, %s, %s" % (self.province, self.city, self.county)

    class Meta:
        verbose_name = u'商家所在地区'
        verbose_name_plural = u'地区列表'

class ShopType(models.Model):
    ShopType = models.CharField(max_length = 10, verbose_name=u'商家类型')

    def __unicode__(self):
        return self.ShopType

    class Meta:
        verbose_name = u'商家类型'
        verbose_name_plural = u'商家类型列表'

class ContactInfo(models.Model):
    Name = models.CharField(max_length = 10, verbose_name=u'联系人姓名')
    Duty = models.CharField(max_length = 10, verbose_name=u'联系人职务')
    Phone = models.CharField(max_length = 15, verbose_name=u'联系人电话')
    Email = models.EmailField(max_length = 20, verbose_name=u'电子邮箱')

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = u'联系人信息'
        verbose_name_plural = u'联系人信息列表'

class ChainStoreInfo(models.Model):
    Name = models.CharField(max_length = 10, verbose_name=u'连锁店名称')
    Address = models.CharField(max_length = 30, verbose_name=u'连锁店地址')
    ContactName = models.CharField(max_length = 10, verbose_name=u'连锁店联系人姓名')
    ContactPhone = models.CharField(max_length = 13, verbose_name=u'连锁店联系人电话')

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = u'连锁店信息'
        verbose_name_plural = u'连锁店信息列表'

class ShopInfo(models.Model):
    ShopName = models.CharField(max_length=20, unique=True, verbose_name=u'商家名称')
    MacAddressList = models.ManyToManyField(MacAddressInfo, verbose_name=u'Mac地址')
    ShopDistrict = models.ForeignKey(DistrictInfo, verbose_name=u'商家所在地区', related_name = "shops")
    ShopDetailAddress = models.CharField(max_length = 100, verbose_name=u'商家详细地址')
    ShopType = models.ForeignKey(ShopType, verbose_name=u'商家类型')
    ContactInfoList = models.ManyToManyField(ContactInfo, verbose_name=u'商家联系人信息')
    IsChainShop = models.BooleanField(default=False, verbose_name=u'是否连锁')
    ChainShopInfo = models.ForeignKey(ChainStoreInfo, blank=True, null=True, verbose_name=u'连锁店信息(若非连锁，请置空)')

    def __unicode__(self):
        return self.ShopName

    class Meta:
        verbose_name = u'商家信息'
        verbose_name_plural = u'商家信息列表'
