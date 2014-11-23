# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0004_auto_20141122_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopinfo',
            name='ChainShopInfo',
            field=models.ForeignKey(verbose_name='\u8fde\u9501\u5e97\u4fe1\u606f', to='ShopInfoCollectorApp.ChainStoreInfo', null=True),
            preserve_default=True,
        ),
    ]
