# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0005_auto_20141122_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='ChainShopInfo',
            field=models.ForeignKey(default=None, verbose_name='\u8fde\u9501\u5e97\u4fe1\u606f', blank=True, to='ShopInfoCollectorApp.ChainStoreInfo'),
            preserve_default=False,
        ),
    ]
