# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20180701_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
