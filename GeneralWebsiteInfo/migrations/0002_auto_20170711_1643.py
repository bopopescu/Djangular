# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-11 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralWebsiteInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootScreenLoader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_layout', max_length=255, unique=True)),
                ('html_code', models.TextField()),
                ('enabled', models.BooleanField(default=True, help_text='check to enable this, only one item is allowed to be enabled')),
            ],
        ),
        migrations.CreateModel(
            name='NavigationBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_layout', max_length=255, unique=True)),
                ('title', models.TextField()),
                ('logo_html_code', models.TextField()),
                ('enabled', models.BooleanField(default=True, help_text='check to enable this, only one item is allowed to be enabled')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteColorTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=255, unique=True)),
                ('css_code', models.TextField()),
                ('enabled', models.BooleanField(default=True, help_text='check to enable this, only one item is allowed to be enabled')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_layout', max_length=255, unique=True)),
                ('style', models.TextField()),
                ('mode', models.TextField()),
                ('enabled', models.BooleanField(default=True, help_text='check to enable this, only one item is allowed to be enabled')),
            ],
        ),
        migrations.DeleteModel(
            name='WebsiteBasicInfo',
        ),
    ]