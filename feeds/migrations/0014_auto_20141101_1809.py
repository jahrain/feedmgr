# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0013_auto_20141101_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
