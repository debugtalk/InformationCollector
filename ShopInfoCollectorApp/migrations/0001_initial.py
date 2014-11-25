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
                ('store_name', models.CharField(max_length=10, verbose_name='\u8fde\u9501\u5e97\u540d\u79f0')),
                ('store_adress', models.CharField(max_length=30, verbose_name='\u8fde\u9501\u5e97\u5730\u5740')),
                ('contact_name', models.CharField(max_length=10, verbose_name='\u8fde\u9501\u5e97\u8054\u7cfb\u4eba\u59d3\u540d')),
                ('contact_phone', models.CharField(max_length=13, verbose_name='\u8fde\u9501\u5e97\u8054\u7cfb\u4eba\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u8fde\u9501\u5e97\u4fe1\u606f',
                'verbose_name_plural': '\u8fde\u9501\u5e97\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
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
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u8054\u7cfb\u4eba\u59d3\u540d')),
                ('duty', models.CharField(max_length=10, verbose_name='\u8054\u7cfb\u4eba\u804c\u52a1')),
                ('phone', models.CharField(max_length=15, verbose_name='\u8054\u7cfb\u4eba\u7535\u8bdd')),
                ('email', models.EmailField(max_length=20, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u4eba\u4fe1\u606f',
                'verbose_name_plural': '\u8054\u7cfb\u4eba\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
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
                ('city', models.ForeignKey(verbose_name='\u57ce\u5e02', to='ShopInfoCollectorApp.City')),
                ('county', models.ForeignKey(verbose_name='\u533a\uff0f\u53bf', to='ShopInfoCollectorApp.County')),
            ],
            options={
                'verbose_name': '\u5546\u5bb6\u6240\u5728\u5730\u533a',
                'verbose_name_plural': '\u5730\u533a\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MacAddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(unique=True, max_length=48, verbose_name='Mac\u5730\u5740')),
            ],
            options={
                'verbose_name': 'Mac\u5730\u5740',
                'verbose_name_plural': 'Mac\u5730\u5740\u5217\u8868',
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
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_name', models.CharField(unique=True, max_length=20, verbose_name='\u5546\u5bb6\u540d\u79f0')),
                ('shop_address', models.CharField(max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('is_chain_shop', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8fde\u9501')),
                ('chain_store_info', models.ForeignKey(verbose_name='\u8fde\u9501\u5e97\u4fe1\u606f(\u82e5\u975e\u8fde\u9501\uff0c\u8bf7\u7f6e\u7a7a)', blank=True, to='ShopInfoCollectorApp.ChainStoreInfo', null=True)),
                ('contact_info_list', models.ManyToManyField(to='ShopInfoCollectorApp.ContactInfo', verbose_name='\u5546\u5bb6\u8054\u7cfb\u4eba\u4fe1\u606f')),
                ('mac_address_list', models.ManyToManyField(to='ShopInfoCollectorApp.MacAddressInfo', verbose_name='Mac\u5730\u5740')),
                ('shop_district', models.ForeignKey(related_name='shops', verbose_name='\u5546\u5bb6\u6240\u5728\u5730\u533a', to='ShopInfoCollectorApp.DistrictInfo')),
            ],
            options={
                'verbose_name': '\u5546\u5bb6\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u5bb6\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_type', models.CharField(max_length=10, verbose_name='\u5546\u5bb6\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u5546\u5bb6\u7c7b\u578b',
                'verbose_name_plural': '\u5546\u5bb6\u7c7b\u578b\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='shop_type',
            field=models.ForeignKey(verbose_name='\u5546\u5bb6\u7c7b\u578b', to='ShopInfoCollectorApp.ShopType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='districtinfo',
            name='province',
            field=models.ForeignKey(verbose_name='\u7701\u4efd', to='ShopInfoCollectorApp.Province'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(related_name='cities', to='ShopInfoCollectorApp.Province'),
            preserve_default=True,
        ),
    ]
