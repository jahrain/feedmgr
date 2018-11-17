# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20141101_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='is_completed',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='torrent_url',
            field=models.URLField(unique=True, max_length=1024, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='downloaddirectory',
            name='location',
            field=models.FilePathField(path=b'/', unique=True, max_length=1024, allow_files=False, allow_folders=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='downloaddirectory',
            name='name',
            field=models.CharField(unique=True, max_length=128, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='feed_url',
            field=models.URLField(unique=True, max_length=1024, db_index=True),
            preserve_default=True,
        ),
    ]
