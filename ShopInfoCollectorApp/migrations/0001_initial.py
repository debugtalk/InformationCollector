# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChainStoreInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=30)),
                ('ContactName', models.CharField(max_length=10)),
                ('ContactPhone', models.CharField(max_length=13)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=10)),
                ('Duty', models.CharField(max_length=10)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Province', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=10)),
                ('County', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MacAddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MacAddress', models.CharField(unique=True, max_length=48)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ShopName', models.CharField(unique=True, max_length=20)),
                ('ShopDetailAddress', models.CharField(max_length=100)),
                ('IsChainShop', models.BooleanField(default=False)),
                ('ChainShopInfo', models.ForeignKey(to='ShopInfoCollectorApp.ChainStoreInfo')),
                ('ContactInfoList', models.ManyToManyField(to='ShopInfoCollectorApp.ContactInfo')),
                ('MacAddressList', models.ManyToManyField(to='ShopInfoCollectorApp.MacAddressInfo')),
                ('ShopDistrict', models.ForeignKey(to='ShopInfoCollectorApp.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ShopType', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='ShopType',
            field=models.ForeignKey(to='ShopInfoCollectorApp.ShopType'),
            preserve_default=True,
        ),
    ]
