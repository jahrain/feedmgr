# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0014_auto_20141101_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='sub_directory',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
