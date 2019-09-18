# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20181024_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='rel',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432\u043d\u0443\u0442\u0440\u0438 rel', blank=True),
            preserve_default=True,
        ),
    ]
