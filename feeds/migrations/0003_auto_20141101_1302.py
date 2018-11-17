# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20141101_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('torrent_url', models.URLField(unique=True, max_length=1024)),
                ('is_completed', models.BooleanField()),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(null=True, blank=True)),
                ('directory', models.ForeignKey(to='feeds.DownloadDirectory')),
                ('subscription', models.ForeignKey(to='feeds.Subscription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='feed_url',
            field=models.URLField(max_length=1024),
            preserve_default=True,
        ),
    ]
