# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20141101_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaddirectory',
            name='location',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
    ]
