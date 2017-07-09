# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 08:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 8, 16, 45, 910203, tzinfo=utc), verbose_name='published_date'),
        ),
    ]