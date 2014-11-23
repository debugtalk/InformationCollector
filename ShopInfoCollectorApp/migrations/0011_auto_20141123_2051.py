# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0010_auto_20141123_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='districtinfo',
            options={'verbose_name': '\u5546\u5bb6\u6240\u5728\u5730\u533a', 'verbose_name_plural': '\u5730\u533a\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='city',
            field=models.ForeignKey(related_name='districtinfos', verbose_name='\u57ce\u5e02', blank=True, to='ShopInfoCollectorApp.City', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='county',
            field=models.ForeignKey(related_name='districtinfos', verbose_name='\u533a\uff0f\u53bf', blank=True, to='ShopInfoCollectorApp.County', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='province',
            field=models.ForeignKey(related_name='districtinfos', verbose_name='\u7701\u4efd', blank=True, to='ShopInfoCollectorApp.Province', null=True),
            preserve_default=True,
        ),
    ]
