# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainstoreinfo',
            name='Address',
            field=models.CharField(max_length=30, verbose_name='\u8fde\u9501\u5e97\u5730\u5740'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chainstoreinfo',
            name='ContactName',
            field=models.CharField(max_length=10, verbose_name='\u8fde\u9501\u5e97\u8054\u7cfb\u4eba\u59d3\u540d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chainstoreinfo',
            name='ContactPhone',
            field=models.CharField(max_length=13, verbose_name='\u8fde\u9501\u5e97\u8054\u7cfb\u4eba\u7535\u8bdd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chainstoreinfo',
            name='Name',
            field=models.CharField(max_length=10, verbose_name='\u8fde\u9501\u5e97\u540d\u79f0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='Duty',
            field=models.CharField(max_length=10, verbose_name='\u8054\u7cfb\u4eba\u804c\u52a1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='Email',
            field=models.EmailField(max_length=20, verbose_name='\u7535\u5b50\u90ae\u7bb1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='Name',
            field=models.CharField(max_length=10, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='Phone',
            field=models.CharField(max_length=15, verbose_name='\u8054\u7cfb\u4eba\u7535\u8bdd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='district',
            name='City',
            field=models.CharField(max_length=10, verbose_name='\u57ce\u5e02'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='district',
            name='County',
            field=models.CharField(max_length=10, verbose_name='\u533a\uff0f\u53bf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='district',
            name='Province',
            field=models.CharField(max_length=10, verbose_name='\u7701\u4efd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='macaddressinfo',
            name='MacAddress',
            field=models.CharField(unique=True, max_length=48, verbose_name='Mac\u5730\u5740'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ChainShopInfo',
            field=models.ForeignKey(verbose_name='\u8fde\u9501\u5e97\u4fe1\u606f', to='ShopInfoCollectorApp.ChainStoreInfo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ContactInfoList',
            field=models.ManyToManyField(to='ShopInfoCollectorApp.ContactInfo', verbose_name='\u5546\u5bb6\u8054\u7cfb\u4eba\u4fe1\u606f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='IsChainShop',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8fde\u9501'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='MacAddressList',
            field=models.ManyToManyField(to='ShopInfoCollectorApp.MacAddressInfo', verbose_name='Mac\u5730\u5740'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ShopDetailAddress',
            field=models.CharField(max_length=100, verbose_name='\u5546\u5bb6\u8be6\u7ec6\u5730\u5740'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ShopDistrict',
            field=models.ForeignKey(verbose_name='\u5546\u5bb6\u6240\u5728\u5730\u533a', to='ShopInfoCollectorApp.District'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ShopName',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u5546\u5bb6\u540d\u79f0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='ShopType',
            field=models.ForeignKey(verbose_name='\u5546\u5bb6\u7c7b\u578b', to='ShopInfoCollectorApp.ShopType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shoptype',
            name='ShopType',
            field=models.CharField(max_length=10, verbose_name='\u5546\u5bb6\u7c7b\u578b'),
            preserve_default=True,
        ),
    ]
