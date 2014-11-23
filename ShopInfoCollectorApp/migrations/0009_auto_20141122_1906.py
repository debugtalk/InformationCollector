# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0008_remove_shopinfo_ischainshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='ChainShopInfo',
            field=models.ForeignKey(verbose_name='\u8fde\u9501\u5e97\u4fe1\u606f(\u82e5\u975e\u8fde\u9501\uff0c\u8bf7\u7f6e\u7a7a)', blank=True, to='ShopInfoCollectorApp.ChainStoreInfo', null=True),
            preserve_default=True,
        ),
    ]
