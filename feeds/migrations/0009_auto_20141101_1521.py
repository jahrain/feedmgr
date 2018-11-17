# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0008_auto_20141101_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='settings_name',
            new_name='name',
        ),
    ]
