# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('comment_text', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=512, unique=True)),
                ('item_price', models.IntegerField(default='100')),
                ('release_date', models.DateField(default='2016-12-12')),
                ('item_status', models.CharField(choices=[('a', 'Avialable'), ('na', 'Not Avialable')], max_length=2)),
                ('item_tags', models.CharField(max_length=512)),
                ('item_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default='2016-12-12')),
                ('order_adress', models.CharField(default='None', max_length=100)),
                ('order_status', models.CharField(choices=[('p', 'Packing'), ('d', 'Delivering'), ('dd', 'Delivered')], max_length=2)),
                ('order_comment', models.TextField(blank=True, max_length=512)),
                ('item_count', models.ManyToManyField(related_name='p', to='blog.Items')),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default='email@example.com', max_length=512, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='Lastname', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='login',
            field=models.CharField(default='login', max_length=512, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Items'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users'),
        ),
    ]
