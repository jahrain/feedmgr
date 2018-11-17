# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_auto_20141101_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=128, null=True, db_index=True),
            preserve_default=True,
        ),
    ]
