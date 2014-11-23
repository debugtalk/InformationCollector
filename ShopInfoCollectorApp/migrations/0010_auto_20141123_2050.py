# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopInfoCollectorApp', '0009_auto_20141122_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(related_name='counties', to='ShopInfoCollectorApp.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistrictInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.ForeignKey(related_name='profiles', verbose_name='\u57ce\u5e02', blank=True, to='ShopInfoCollectorApp.City', null=True)),
                ('county', models.ForeignKey(related_name='profiles', verbose_name='\u533a\uff0f\u53bf', blank=True, to='ShopInfoCollectorApp.County', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='districtinfo',
            name='province',
            field=models.ForeignKey(related_name='profiles', verbose_name='\u7701\u4efd', blank=True, to='ShopInfoCollectorApp.Province', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(related_name='cities', to='ShopInfoCollectorApp.Province'),
            preserve_default=True,
        ),
    ]
