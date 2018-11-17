# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_auto_20141101_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='directory',
        ),
        migrations.AddField(
            model_name='download',
            name='hash',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='download',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='download',
            name='name',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
    ]
