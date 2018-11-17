# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_subscription_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='last_active',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
