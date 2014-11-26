# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0002_auto_20141126_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoptype',
            name='shop_type',
            field=models.CharField(unique=True, max_length=10, verbose_name='\u5546\u5bb6\u7c7b\u578b'),
            preserve_default=True,
        ),
    ]
