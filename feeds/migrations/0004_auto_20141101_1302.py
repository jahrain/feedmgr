# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20141101_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='is_completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
