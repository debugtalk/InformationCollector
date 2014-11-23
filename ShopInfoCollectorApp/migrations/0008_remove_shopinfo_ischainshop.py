# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0007_auto_20141122_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopinfo',
            name='IsChainShop',
        ),
    ]
