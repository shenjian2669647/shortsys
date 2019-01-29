# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=50)),
                ('slug', models.SlugField(verbose_name='Slug', unique=True)),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(verbose_name='是否激活', default=True)),
                ('meta_keywords', models.CharField(verbose_name='Meta关键词', max_length=255)),
                ('meta_description', models.CharField(verbose_name='Meta描述', max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='创建日期', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新日期', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=255, unique=True)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=255, unique=True)),
                ('brand', models.CharField(verbose_name='品牌', max_length=50)),
                ('sku', models.CharField(verbose_name='计量单位', max_length=50)),
                ('price', models.DecimalField(verbose_name='价格', max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(verbose_name='旧价格', blank=True, default=0.0, max_digits=9, decimal_places=2)),
                ('image', models.ImageField(verbose_name='图片', max_length=50, upload_to='')),
                ('is_active', models.BooleanField(verbose_name='设为激活', default=True)),
                ('is_bestseller', models.BooleanField(verbose_name='标为畅销', default=False)),
                ('is_featured', models.BooleanField(verbose_name='标为推荐', default=False)),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(verbose_name='Meta关键词', max_length=255)),
                ('meta_description', models.CharField(verbose_name='Meta描述', max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='创建日期', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新日期', auto_now=True)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
