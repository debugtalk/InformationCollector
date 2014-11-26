# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='province',
        ),
        migrations.RemoveField(
            model_name='county',
            name='city',
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='city',
            field=models.CharField(max_length=10, verbose_name='\u57ce\u5e02'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='county',
            field=models.CharField(max_length=10, verbose_name='\u533a\uff0f\u53bf'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='County',
        ),
        migrations.AlterField(
            model_name='districtinfo',
            name='province',
            field=models.CharField(max_length=10, verbose_name='\u7701\u4efd'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Province',
        ),
        migrations.AlterField(
            model_name='shopinfo',
            name='shop_district',
            field=models.ForeignKey(verbose_name='\u5546\u5bb6\u6240\u5728\u5730\u533a', to='ShopInfoCollectorApp.DistrictInfo'),
            preserve_default=True,
        ),
    ]
