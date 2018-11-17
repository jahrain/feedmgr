# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_subscription_last_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='notify_email',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
    ]
