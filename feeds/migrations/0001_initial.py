# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadDirectory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('location', models.FilePathField(path=b'/', max_length=1024, allow_files=False, allow_folders=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('settings_name', models.CharField(default=b'global', max_length=40, serialize=False, primary_key=True)),
                ('transmission_rpc_host', models.GenericIPAddressField()),
                ('transmission_rpc_port', models.IntegerField()),
                ('transmission_rpc_user', models.CharField(max_length=40)),
                ('transmission_rpc_password', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feed_url', models.URLField()),
                ('download_to', models.ForeignKey(to='feeds.DownloadDirectory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
