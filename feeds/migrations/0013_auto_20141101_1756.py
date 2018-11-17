# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0012_subscription_notify_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='notify_email',
        ),
        migrations.AddField(
            model_name='subscription',
            name='notify_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
