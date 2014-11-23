# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0003_auto_20141122_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chainstoreinfo',
            options={'verbose_name': '\u8fde\u9501\u5e97\u4fe1\u606f', 'verbose_name_plural': '\u8fde\u9501\u5e97\u4fe1\u606f\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': '\u8054\u7cfb\u4eba\u4fe1\u606f', 'verbose_name_plural': '\u8054\u7cfb\u4eba\u4fe1\u606f\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': '\u5546\u5bb6\u6240\u5728\u5730\u533a', 'verbose_name_plural': '\u5730\u533a\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='macaddressinfo',
            options={'verbose_name': 'Mac\u5730\u5740', 'verbose_name_plural': 'Mac\u5730\u5740\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='shopinfo',
            options={'verbose_name': '\u5546\u5bb6\u4fe1\u606f', 'verbose_name_plural': '\u5546\u5bb6\u4fe1\u606f\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='shoptype',
            options={'verbose_name': '\u5546\u5bb6\u7c7b\u578b', 'verbose_name_plural': '\u5546\u5bb6\u7c7b\u578b\u5217\u8868'},
        ),
    ]
