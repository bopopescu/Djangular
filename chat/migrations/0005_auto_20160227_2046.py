# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_linkmessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkmessage',
            old_name='iamge_url',
            new_name='image_url',
        ),
    ]
