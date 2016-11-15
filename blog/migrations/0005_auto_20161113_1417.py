# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161113_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Item_Orders',
            new_name='ItemOrders',
        ),
        migrations.AddField(
            model_name='items',
            name='item_name',
            field=models.CharField(default='ItemExample', max_length=512, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='item_price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=512, unique=True),
        ),
    ]