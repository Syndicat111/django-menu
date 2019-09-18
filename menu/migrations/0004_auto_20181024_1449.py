# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20160401_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='extra',
            field=models.CharField(max_length=120, null=True, verbose_name='Extra parameters', blank=True),
            preserve_default=True,
        ),
    ]
