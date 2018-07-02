# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20180701_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to='lists.List'),
        ),
    ]
